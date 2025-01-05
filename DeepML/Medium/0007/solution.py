"""
Platform: DeepML
Problem: 7 - Matrix Transformation
Difficulty: Medium
URL: https://www.deep-ml.com/problems/7

Date: 2025-01-01
Time: 12:28

Author: Kyire
"""

import numpy as np


def transform_matrix(
    A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]
) -> list[list[int | float]]:
    A, T, S = np.array(A), np.array(T), np.array(S)

    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        return -1

    return np.dot(np.dot(np.linalg.inv(T), A), S).tolist()
