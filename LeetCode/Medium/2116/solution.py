"""
Platform: LeetCode
Problem: 2116 - Check if a Parentheses String Can Be Valid
Difficulty: Medium
URL: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
Date: 2025-03-23
Time: 14:23

Author: Kyrie

Algorithm: Greedy
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 67 ms
Memory: 18 MB
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        minv = maxv = 0

        for ch, lock in zip(s, locked):
            if lock == "1":
                diff = 1 if ch == "(" else -1
                maxv += diff
                minv += diff
                if maxv < 0:
                    return False
            else:
                maxv += 1
                minv -= 1

            if minv < 0:
                minv = 1

        return minv == 0
