"""
Platform: LeetCode
Problem: 922 - Sort Array By Parity II
Difficulty: Easy
URL: https://leetcode.com/problems/sort-array-by-parity-ii/

Date: 2025-02-04
Time: 17:01

Author: Kyire

Algorithm: Math
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 7 ms
Memory: 18.66 MB
"""


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even, odd = 0, 1

        while even < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2

        return nums
