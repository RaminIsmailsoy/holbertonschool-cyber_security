#!/usr/bin/python3
"""
read_write_heap.py - Find and replace a string in the heap of a running process.

Usage: read_write_heap.py pid search_string replace_string
"""

import sys
import os


def print_usage_and_exit():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def find_heap_region(pid):
    """
    Parse /proc/pid/maps to find the [heap] region.
    Returns (start_addr, end_addr) as integers, or None if not found.
    """
    maps_path = "/proc/{}/maps".format(pid)

    try:
        with open(maps_path, "r") as maps_file:
            for line in maps_file:
                # Each line looks like:
                # 55a1b2c3d000-55a1b2c3e000 rw-p 00000000 00:00 0  [heap]
                if "[heap]" in line:
                    # Parse the address range (first field)
                    addr_range = line.split()[0]          # e.g. "55a1b2c3d000-55a1b2c3e000"
                    start_str, end_str = addr_range.split("-")
                    start_addr = int(start_str, 16)
                    end_addr   = int(end_str,   16)
                    print("[*] Found heap: 0x{:x} - 0x{:x} ({} bytes)".format(
                        start_addr, end_addr, end_addr - start_addr))
                    return start_addr, end_addr
    except PermissionError:
        print("Error: Permission denied reading {}".format(maps_path))
        sys.exit(1)
    except FileNotFoundError:
        print("Error: No such process with pid {}".format(pid))
        sys.exit(1)

    return None


def read_heap(pid, start_addr, end_addr):
    """Read the heap region from /proc/pid/mem."""
    mem_path = "/proc/{}/mem".format(pid)
    heap_size = end_addr - start_addr

    try:
        with open(mem_path, "rb") as mem_file:
            mem_file.seek(start_addr)
            heap_data = mem_file.read(heap_size)
        return heap_data
    except PermissionError:
        print("Error: Permission denied reading {}".format(mem_path))
        sys.exit(1)
    except OSError as e:
        print("Error reading process memory: {}".format(e))
        sys.exit(1)


def write_heap(pid, start_addr, offset, data):
    """Write patched bytes back to /proc/pid/mem at the exact offset."""
    mem_path = "/proc/{}/mem".format(pid)

    try:
        with open(mem_path, "rb+") as mem_file:
            mem_file.seek(start_addr + offset)
            mem_file.write(data)
    except PermissionError:
        print("Error: Permission denied writing to {}".format(mem_path))
        sys.exit(1)
    except OSError as e:
        print("Error writing to process memory: {}".format(e))
        sys.exit(1)


def main():
    # ── Argument validation ──────────────────────────────────────────────────
    if len(sys.argv) != 4:
        print_usage_and_exit()

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: pid must be an integer")
        print_usage_and_exit()

    search_string  = sys.argv[2]
    replace_string = sys.argv[3]

    if len(replace_string) > len(search_string):
        print("Error: replace_string must not be longer than search_string "
              "(to avoid overwriting adjacent memory)")
        sys.exit(1)

    search_bytes  = search_string.encode("ASCII")
    # Pad replacement with null bytes so we always write the same number of bytes
    replace_bytes = replace_string.encode("ASCII").ljust(len(search_bytes), b"\x00")

    print("[*] PID          : {}".format(pid))
    print("[*] Search string: {!r}".format(search_string))
    print("[*] Replace with : {!r}".format(replace_string))

    # ── Locate heap ──────────────────────────────────────────────────────────
    result = find_heap_region(pid)
    if result is None:
        print("Error: Could not find [heap] region for pid {}".format(pid))
        sys.exit(1)

    start_addr, end_addr = result

    # ── Read heap ────────────────────────────────────────────────────────────
    heap_data = read_heap(pid, start_addr, end_addr)
    print("[*] Heap read: {} bytes".format(len(heap_data)))

    # ── Search ───────────────────────────────────────────────────────────────
    offset = heap_data.find(search_bytes)
    if offset == -1:
        print("[!] String {!r} not found in heap".format(search_string))
        sys.exit(1)

    abs_addr = start_addr + offset
    print("[*] Found {!r} at heap offset 0x{:x} (absolute addr 0x{:x})".format(
        search_string, offset, abs_addr))

    # ── Write ────────────────────────────────────────────────────────────────
    write_heap(pid, start_addr, offset, replace_bytes)
    print("[*] Replaced with {!r} — done!".format(replace_string))


if __name__ == "__main__":
    main()
