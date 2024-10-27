"""
Platform: LeetCode
Problem: 684 - Redundant Connection
Difficulty: Medium
URL: https://leetcode.com/problems/redundant-connection

Date: 2024-10-27
Time: 10:12

Author: Kyrie

Algorithm: Union Find
Time Complexity: O(nlogn)
Space Complexity: O(n)

Runtime: 0 ms
Memory: 16.86 MB
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n + 1))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        res = []
        for a, b in edges:
            if find(a) != find(b):
                p[find(a)] = find(b)
            else:
                res = [a, b]

        return res
