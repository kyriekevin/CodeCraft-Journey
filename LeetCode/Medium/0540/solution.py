"""
Platform: LeetCode
Problem: 540 - Single Element in a Sorted Array
Difficulty: Medium
URL: https://leetcode.com/problems/single-element-in-a-sorted-array/

Date: 2024-11-10
Time: 09:53

Author: Kyrie

Algorithm: Binary Search
Time Complexity: O(logn)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 23.50 MB
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] != nums[mid ^ 1]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
