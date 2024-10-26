"""
Platform: DeepML
Problem: 4 - Calculate Mean by Row or Column
Difficulty: Easy
URL: https://www.deep-ml.com/problem/Calculate%20Mean%20by%20Row%20or%20Column

Date: 2024-10-26
Time: 17:59

Author: Kyire
"""


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = [sum(row) / len(row) for row in matrix]
    else:
        means = [sum(col) / len(col) for col in zip(*matrix)]
    return means
