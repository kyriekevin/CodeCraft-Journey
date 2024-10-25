"""
Platform: LeetCode
Problem: 3180 - Maximum Total Reward Using Operations I
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-total-reward-using-operations-i

Date: 2024-10-25
Time: 20:16

Author: Kyrie

Algorithm: Dynamic Programming
Time Complexity: O(n * maxv)
Space Complexity: O(n * maxv)

Runtime: 3360 ms
Memory: 77.80 MB
"""


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        n = len(rewardValues)
        rewardValues.sort()
        maxv = rewardValues[-1] * 2
        f = [[False] * maxv for _ in range(n + 1)]
        f[0][0] = True

        for i in range(1, n + 1):
            x = rewardValues[i - 1]
            for j in range(2 * x - 1, -1, -1):
                f[i][j] = f[i - 1][j]
                if j >= x:
                    f[i][j] |= f[i - 1][j - x]

        res = maxv - 1
        while not f[n][res]:
            res -= 1

        return res
