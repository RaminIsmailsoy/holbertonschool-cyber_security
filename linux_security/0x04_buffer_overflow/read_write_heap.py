#!/usr/bin/python3
"""
read_write_heap.py - Find and replace a string in the heap of a running process.

Usage: read_write_heap.py pid search_string replace_string
"""

import sys


def print_usage_and_exit():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def find_heap_region(pid):
    """Parse /proc/pid/maps and return (start, end) of [heap], or None."""
    maps_path = "/proc/{}/maps".format(pid)
    try:
        with open(maps_path, "r") as f:
            for line in f:
                if "[heap]" in line:
                    addr_range = line.split()[0]
                    start_str, end_str = addr_range.split("-")
                    return int(start_str, 16), int(end_str, 16)
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
    try:
        with open(mem_path, "rb") as f:
            f.seek(start_addr)
            return f.read(end_addr - start_addr)
    except PermissionError:
        print("Error: Permission denied reading {}".format(mem_path))
        sys.exit(1)
    except OSError as e:
        print("Error reading process memory: {}".format(e))
        sys.exit(1)


def write_heap(pid, start_addr, offset, data):
    """Write patched bytes to /proc/pid/mem at the given offset."""
    mem_path = "/proc/{}/mem".format(pid)
    try:
        with open(mem_path, "rb+") as f:
            f.seek(start_addr + offset)
            f.write(data)
    except PermissionError:
        print("Error: Permission denied writing to {}".format(mem_path))
        sys.exit(1)
    except OSError as e:
        print("Error writing to process memory: {}".format(e))
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print_usage_and_exit()

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: pid must be an integer")
        print_usage_and_exit()

    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if len(replace_string) > len(search_string):
        print("Error: replace_string must not be longer than search_string")
        sys.exit(1)

    search_bytes = search_string.encode("ASCII")
    replace_bytes = replace_string.encode("ASCII").ljust(len(search_bytes), b"\x00")

    result = find_heap_region(pid)
    if result is None:
        print("Error: Could not find [heap] region for pid {}".format(pid))
        sys.exit(1)

    start_addr, end_addr = result
    heap_data = read_heap(pid, start_addr, end_addr)

    offset = heap_data.find(search_bytes)
    if offset == -1:
        print("Error: String {!r} not found in heap".format(search_string))
        sys.exit(1)

    write_heap(pid, start_addr, offset, replace_bytes)
    print("SUCCESS!")


if __name__ == "__main__":
    main()
