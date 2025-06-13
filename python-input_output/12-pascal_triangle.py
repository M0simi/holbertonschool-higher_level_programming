#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
