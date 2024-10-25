# 3180 - Maximum Total Reward Using Operations I

## Problem Description

```plaintext
You are given an integer array rewardValues of length n, representing the values of rewards.

Initially, your total reward x is 0, and all indices are unmarked. You are allowed to perform the following operation any number of times:

Choose an unmarked index i from the range [0, n - 1].
If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x (i.e., x = x + rewardValues[i]), and mark the index i.
Return an integer denoting the maximum total reward you can collect by performing the operations optimally.
```

- Difficulty: Medium
- URL: https://leetcode.com/problems/maximum-total-reward-using-operations-i

## Examples

> Input: rewardValues = [1,1,3,3]
>
> Output: 4
>
> Explanation:
>
> During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

## Approach

```plaintext
1. Sort the array in ascending order.
2. dp[i][j] = True if the maximum total reward is j using the first i rewards.
3. dp[i][j] = dp[i - 1][j] if rewardValues[i] <= j
4. dp[i][j] = dp[i][j] |= dp[i - 1][j - rewardValues[i]] if rewardValues[i] > j
5. The maximum total reward is the maximum value of dp[n][mx] = True.
```


### Complexity Analysis

- Time complexity: O(n * mx)
- Space complexity: O(n * mx)
  - The space complexity is O(n * mx) because a 2D array is used.
