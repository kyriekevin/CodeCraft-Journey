"""
Platform: DeepML
Problem: 1 - Matrix times Vector
Difficulty: Easy
URL: https://www.deep-ml.com/problem/Matrix%20times%20Vector

Date: 2024-10-23
Time: 21:38

Author: Kyire
"""


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    if len(a[0]) != len(b):
        return -1

    res = []
    for i in range(len(a)):
        temp = 0
        for j in range(len(a[i])):
            temp += a[i][j] * b[j]
        res.append(temp)

    return res
