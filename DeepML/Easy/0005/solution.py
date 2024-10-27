"""
Platform: DeepML
Problem: 5 - Scalar Multiplication of a Matrix
Difficulty: Easy
URL: https://www.deep-ml.com/problem/Scalar%20Multiplication%20of%20a%20Matrix

Date: 2024-10-27
Time: 10:17

Author: Kyire
"""


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    return [[element * scalar for element in row] for row in matrix]
