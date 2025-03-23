"""
Platform: DeepML
Problem: 44 - Leaky RuLU Activation Function
Difficulty: Easy
URL: https://www.deep-ml.com/problems/44

Date: 2025-03-22
Time: 15:07

Author: Kyire
"""


def leaky_relu(z: float, alpha: float = 0.01) -> float | int:
    if z >= 0:
        return z
    else:
        return z * alpha
