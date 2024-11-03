"""
Platform: LeetCode
Problem: 3226 - Number of Bit Changes to Make Two Integers Equal
Difficulty: Easy
URL: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal

Date: 2024-11-02
Time: 10:43

Author: Kyire

Algorithm: Math
Time Complexity: O(1)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 16.47 MB
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return -1 if n & k != k else (n ^ k).bit_count()
