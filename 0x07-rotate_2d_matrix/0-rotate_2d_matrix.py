#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    This function modifies the input matrix in-place by performing a
    90-degree clockwise rotation. The rotation is done by a 4-way swap
    of the elements in layers from the outermost to the innermost.

    Time Complexity: O(n^2), where n is the number of rows (or columns) in the matrix.
    Space Complexity: O(1), as the rotation is performed in-place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.

    Returns:
        None: The matrix is rotated in-place, and nothing is returned.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Perform 4-way swap
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
