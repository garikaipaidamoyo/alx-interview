#!/usr/bin/python3

def pascal_triangle(n):
    if not isinstance(n, int) or n <= 0:
        return []  # Return an empty list for non-integer or n <= 0

    triangle = []  # Initialize an empty list to store the triangle

    for i in range(n):
        row = []  # Initialize a new row for each iteration
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # The first and last elements in each row are 1
            else:
                # Calculate the elements in between based on the previous row
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)
        triangle.append(row)  # Add the row to the triangle

    return triangle

# Testing the function
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
