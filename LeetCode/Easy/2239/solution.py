"""
Platform: LeetCode
Problem: 2239 - find closest number to zero
Difficulty: Easy
URL: https://leetcode.com/problems/find-closest-number-to-zero/description/

Date: 2025-01-20
Time: 23:52

Author: Kyire

Algorithm: Array
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 8 ms
Memory: 17.9 MB
"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for x in nums:
            if abs(x) < abs(res) or (abs(x) == abs(res) and x > 0):
                res = x
        return res
