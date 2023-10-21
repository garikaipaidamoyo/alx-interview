#!/usr/bin/python3

"""
Log Parsing Script

This script reads log data and computes metrics.

Input format: ...
After every 10 lines...
"""

import sys


def print_stats(total_size, status_counts):
    """Print statistics"""
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        print("{}: {}".format(status, count))


def main():
    total_size = 0
    status_counts = {}

    line_number = 0

    try:
        for line in sys.stdin:
            line = line.strip()

            # Split the line by space
            parts = line.split()

            # Check if the line format is valid
            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = int(parts[-1])

                if status_code.isdigit():
                    status_code = int(status_code)

                    # Update status counts
                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        if status_code in status_counts:
                            status_counts[status_code] += 1
                        else:
                            status_counts[status_code] = 1

                total_size += file_size

            line_number += 1

            if line_number % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
