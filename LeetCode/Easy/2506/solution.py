"""
Platform: LeetCode
Problem: 2506 - Count Pairs Of Similar Strings
Difficulty: Easy
URL: https://leetcode.com/problems/count-pairs-of-similar-strings/

Date: 2025-02-22
Time: 12:54

Author: Kyire

Algorithm: Array
Time Complexity: O(n)
Space Complexity: O(n)

Runtime: 23 ms
Memory: 17.43 MB
"""


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        cnt = defaultdict(int)

        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            res += cnt[mask]
            cnt[mask] += 1

        return res
