#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def find_heap_region(pid):
    maps_path = "/proc/{}/maps".format(pid)
    try:
        with open(maps_path, "r") as f:
            for line in f:
                if "[heap]" in line:
                    addr_range = line.split()[0]
                    start_str, end_str = addr_range.split("-")
                    return int(start_str, 16), int(end_str, 16)
    except Exception:
        pass
    return None


def read_heap(pid, start_addr, end_addr):
    mem_path = "/proc/{}/mem".format(pid)
    try:
        with open(mem_path, "rb") as f:
            f.seek(start_addr)
            return f.read(end_addr - start_addr)
    except Exception:
        return None


def write_heap(pid, start_addr, offset, data):
    mem_path = "/proc/{}/mem".format(pid)
    try:
        with open(mem_path, "rb+") as f:
            f.seek(start_addr + offset)
            f.write(data)
    except Exception:
        return False
    return True


def main():
    if len(sys.argv) != 4:
        print_usage_and_exit()

    try:
        pid = int(sys.argv[1])
    except Exception:
        print_usage_and_exit()

    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if len(replace_string) > len(search_string):
        print_usage_and_exit()

    search_bytes = search_string.encode("ascii")
    replace_bytes = replace_string.encode("ascii").ljust(len(search_bytes), b"\x00")

    heap = find_heap_region(pid)
    if heap is None:
        print_usage_and_exit()

    start_addr, end_addr = heap

    heap_data = read_heap(pid, start_addr, end_addr)
    if heap_data is None:
        print_usage_and_exit()

    offset = heap_data.find(search_bytes)
    if offset == -1:
        print_usage_and_exit()

    if not write_heap(pid, start_addr, offset, replace_bytes):
        print_usage_and_exit()

    print("SUCCESS!")


if __name__ == "__main__":
    main()
