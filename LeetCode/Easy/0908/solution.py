"""
Platform: LeetCode
Problem: 908 - Smallest Range I
Difficulty: Easy
URL: https://leetcode.com/problems/smallest-range-i/description/

Date: 2024-10-20
Time: 22:08

Author: Kyire

Algorithm: Math
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 17.31 MB
"""


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minv, maxv = min(nums), max(nums)

        return max(0, maxv - minv - 2 * k)
