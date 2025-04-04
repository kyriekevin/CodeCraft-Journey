/*
Platform: LeetCode
Problem: 1123 - Lowest Common Ancestor of Deepest Leaves
Difficulty: Medium
URL: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Date: 2025-04-04
Time: 12:14

Author: Kyire

Algorithm: Depth-First Search
Time Complexity: O(n)
Space Complexity: O(n)

Runtime: 0 ms
Memory: 21.5 MB
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#define x first
#define y second

class Solution {
public:
    pair<TreeNode*, int> dfs(TreeNode* root) {
        if (!root) return {root, 0};
        auto left = dfs(root->left), right = dfs(root->right);
        if (left.y > right.y) return {left.x, left.y + 1};
        if (left.y < right.y) return {right.x, right.y + 1};
        return {root, left.y + 1};
    }
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root).x;
    }
};
