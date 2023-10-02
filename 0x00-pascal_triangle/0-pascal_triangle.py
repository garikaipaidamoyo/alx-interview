#!/usr/bin/python3

"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
