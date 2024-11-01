"""
Platform: LeetCode
Problem: 3259 - Maximum Energy Boost From Two Drinks
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

Date: 2024-11-01
Time: 20:10

Author: Kyire

Algorithm: Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)

Runtime: 440 ms
Memory: 45.97 MB
"""


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        f = [[0, 0] for _ in range(n + 2)]

        for i, (x, y) in enumerate(zip(energyDrinkA, energyDrinkB)):
            f[i + 2][0] = max(f[i + 1][0], f[i][1]) + x
            f[i + 2][1] = max(f[i + 1][1], f[i][0]) + y

        return max(f[-1])
