"""
Platform: DeepML
Problem: 8 - Calculate 2x2 Matrix Inverse
Difficulty: Medium
URL: https://www.deep-ml.com/problems/8

Date: 2025-01-04
Time: 11:51

Author: Kyire
"""


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None

    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - b * c

    if det == 0:
        return None

    return [[d / det, -b / det], [-c / det, a / det]]
