#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = []  # Initialize an empty list to store the triangle

    for i in range(n):
        row = []  # Initialize a new row for each iteration
        if i == 0:
            row.append(1)  # The first row starts with 1
        else:
            prev_row = triangle[i - 1]  # Get the previous row
            row.append(1)  # The first element in each row is 1
            for j in range(1, i):
                # Calculate the elements in between based on the previous row
                element = prev_row[j - 1] + prev_row[j]
                row.append(element)
            row.append(1)  # The last element in each row is 1
        triangle.append(row)  # Add the row to the triangle

    return triangle

# Testing the function
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
