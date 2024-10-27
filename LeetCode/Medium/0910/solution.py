"""
Platform: LeetCode
Problem: 910 - Smallest Range II
Difficulty: Medium
URL: https://leetcode.com/problems/smallest-range-ii/

Date: 2024-10-21
Time: 22:02

Author: Kyrie

Algorithm: Greedy
Time Complexity: O(nlogn)
Space Complexity: O(1)

Runtime: 35 ms
Memory: 17.4 MB
"""


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for x, y in pairwise(nums):
            maxv = max(x + k, nums[-1] - k)
            minv = min(nums[0] + k, y - k)
            res = min(res, maxv - minv)

        return res
