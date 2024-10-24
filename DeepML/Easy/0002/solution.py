"""
Platform: DeepML
Problem: 2 - Transpose of a Matrix
Difficulty: Easy
URL: https://www.deep-ml.com/problem/Transpose%20of%20a%20Matrix

Date: 2024-10-24
Time: 22:33

Author: Kyire
"""


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    # n, m = len(a), len(a[0])
    # res = [[0] * n for _ in range(m)]

    # for i in range(n):
    #     for j in range(m):
    #         res[j][i] = a[i][j]

    # return res

    return [list(row) for row in zip(*a)]
