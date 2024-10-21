# 910 - Smallest Range II

## Problem Description

You are given an integer array nums and an integer k.

For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after changing the values at each index.

- Difficulty: Medium
- URL: https://leetcode.com/problems/smallest-range-ii/

## Examples

Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

## Approach

I sort the entire array and find the dividing point. If there are smaller numbers on the left side of the dividing point, the +k operation will be performed, and if there are larger numbers on the right side of the dividing point, the -k operation will be performed. The minimum score is calculated by comparing the maximum and minimum values of the array after the operation.

### Complexity Analysis

- Time complexity: O(nlogn)
  - The time complexity is O(nlogn) because the array is sorted.
- Space complexity: O(1)
  - The space complexity is O(1) because no extra space is used.
