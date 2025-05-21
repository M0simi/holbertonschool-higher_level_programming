#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists)
        of integers/floats.
        div (int or float): The number to divide all matrix
        elements by.

    Returns:
        list of lists: A new matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row in the matrix is not the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is 0.

    Examples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
