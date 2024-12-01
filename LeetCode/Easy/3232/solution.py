"""
Platform: LeetCode
Problem: 3232 - Find if Digit Game Can Be Won
Difficulty: Easy
URL: https://leetcode.com/problems/find-if-digit-game-can-be-won/

Date: 2024-11-30
Time: 13:35

Author: Kyire

Algorithm: Math
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 17 MB
"""


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        tot = sum(nums)
        n = len(nums)
        cur_a, cur_b = 0, 0

        for i in range(n):
            if nums[i] < 10:
                cur_a += nums[i]
            elif nums[i] < 100:
                cur_b += nums[i]

        if cur_a * 2 > tot or cur_b * 2 > tot:
            return True

        return False
