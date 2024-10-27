"""
Platform: DeepML
Problem: 3 - Reshape Matrix
Difficulty: Easy
URL: https://www.deep-ml.com/problem/Reshape%20Matrix

Date: 2024-10-25
Time: 21:09

Author: Kyire
"""

import numpy as np


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    return np.array(a).reshape(new_shape).tolist()
