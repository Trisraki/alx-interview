#!/usr/bin/python3
"""0. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """A 2D matrix 90 degrees clockwise function."""
    ziped = zip(*reversed(matrix))
    for i, j in enumerate(ziped):
        matrix[i] = list(j)
