"""
Platform: LeetCode
Problem: 80 - Remove Duplicates from Sorted Array II
Difficulty: Medium
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Date: 2025-02-09
Time: 12:39

Author: Kyrie

Algorithm: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 84 ms
Memory: 20 MB
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        slow = 2
        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
