"""
Platform: LeetCode
Problem: 3184 - Count Pairs That Form a Complete Day
Difficulty: Easy
URL: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i

Date: 2024-10-22
Time: 22:14

Author: Kyire

Algorithm: Math
Time Complexity: O(n + H)
Space Complexity: O(H)

Runtime: 0 ms
Memory: 16.4 MB
"""


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        res = 0

        for i in range(len(hours)):
            r = hours[i] % 24
            res += cnt[(24 - r) % 24]
            cnt[r] += 1

        return res
