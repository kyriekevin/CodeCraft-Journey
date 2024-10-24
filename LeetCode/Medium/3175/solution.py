"""
Platform: LeetCode
Problem: 3175 - Find The First Player to Win K Games in a Row
Difficulty: Medium
URL: https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/

Date: 2024-10-24
Time: 22:24

Author: Kyire

Algorithm: Simulation
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 39 ms
Memory: 29.06 MB
"""


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        max_idx, cnt = 0, 0

        for i in range(1, len(skills)):
            if skills[i] > skills[max_idx]:
                max_idx = i
                cnt = 1
            else:
                cnt += 1

            if cnt == k:
                break

        return max_idx
