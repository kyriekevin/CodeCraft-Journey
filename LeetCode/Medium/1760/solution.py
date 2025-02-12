"""
Platform: LeetCode
Problem: 1760 - Minimum Limit of Balls in a Bag
Difficulty: Medium
URL: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
Date: 2025-02-12
Time: 22:39

Author: Kyrie

Algorithm: Binary Search
Time Complexity: O(nlogn)
Space Complexity: O(1)

Runtime: 519 ms
Memory: 30.3 MB
"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(nums, x, maxOperations):
            if x == 0:
                return False
            cnt = 0
            for num in nums:
                cnt += (num - 1) // x
            return cnt <= maxOperations

        l, r = 0, max(nums)
        while l < r:
            mid = l + r >> 1
            print(l, r, mid)
            if check(nums, mid, maxOperations):
                r = mid
            else:
                l = mid + 1

        return l
