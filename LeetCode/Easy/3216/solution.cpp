/*
Platform: LeetCode
Problem: 3216 - Lexicographically Smallest String After a Swap
Difficulty: Easy
URL: https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap

Date: 2024-10-30
Time: 21:14

Author: Kyire

Algorithm: Greedy
Time Complexity: O(n)
Space Complexity: O(1)

Runtime: 0 ms
Memory: 8.02 MB
*/

class Solution {
public:
    string getSmallestString(string s) {
        for (int i = 1; i < s.size(); i++) {
            char x = s[i - 1], y = s[i];
            if (x > y && x % 2 == y % 2) {
                swap(s[i - 1], s[i]);
                break;
            }
        }

        return s;
    }
};
