/*
Platform: LeetCode
Problem: 368 - Largest Divisible Subset
Difficulty: Medium
URL: https://leetcode.com/problems/largest-divisible-subset/

Date: 2025-04-06
Time: 10:51

Author: Kyire

Algorithm: Dynamic Programming
Time Complexity: O(n^2)
Space Complexity: O(n)

Runtime: 15 ms
Memory: 12.28 MB
*/

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        vector<int> f(n);
        sort(nums.begin(), nums.end());

        int k = 0;
        for (int i = 0; i < n; i++) {
            f[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0)
                    f[i] = max(f[i], f[j] + 1);
            }
            if (f[i] > f[k]) k = i;
        }

        vector<int> res;
        while (true) {
            res.push_back(nums[k]);
            if (f[k] == 1) break;
            for (int i = 0; i < k; i++) {
                if (nums[k] % nums[i] == 0 && f[k] == f[i] + 1) {
                    k = i;
                    break;
                }
            }
        }

        return res;
    }
};
