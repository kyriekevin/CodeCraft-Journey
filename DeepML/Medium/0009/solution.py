"""
Platform: DeepML
Problem: 9 - Matrix times Matrix
Difficulty: Medium
URL: https://www.deep-ml.com/problems/9

Date: 2025-01-05
Time: 11:52

Author: Kyire
"""


def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    if len(a[0]) != len(b):
        return -1

    n, m = len(a), len(b[0])
    res = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(len(a[0])))
    return res
