"""
Platform: DeepML
Problem: 6 - Calculate Eigenvalues of a Matrix
Difficulty: Medium
URL: https://www.deep-ml.com/problem/Calculate%20Eigenvalues%20of%20a%20Matrix

Date: 2024-11-03
Time: 12:37

Author: Kyire
"""


def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace**2 - 4 * determinant
    lambda1 = (trace + discriminant**0.5) / 2
    lambda2 = (trace - discriminant**0.5) / 2

    return [lambda1, lambda2]
