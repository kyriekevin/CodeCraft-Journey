"""
Platform: LeetCode
Problem: 1561 - Maximum Number of Coins You Can Get
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-number-of-coins-you-can-get
Date: 2025-01-22
Time: 23:32

Author: Kyrie

Algorithm: Greedy
Time Complexity: O(nlogn)
Space Complexity: O(1)

Runtime: 70 ms
Memory: 27 MB
"""


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()
        for i in range(len(piles) // 3, len(piles), 2):
            res += piles[i]
        return res
