"""
Platform: LeetCode
Problem: 865 - Smallest Subtree with all the Deepest Nodes
Difficulty: Medium
URL: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

Date: 2024-04-04
Time: 12:22

Author: Kyrie

Algorithm: Depth-First Search
Time Complexity: O(n)
Space Complexity: O(n)

Runtime: 0 ms
Memory: 17.56 MB
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> (Optional[TreeNode], int):
            if node is None:
                return None, 0
            llca, lh = dfs(node.left)
            rlca, rh = dfs(node.right)
            if lh > rh:
                return llca, lh + 1
            elif lh < rh:
                return rlca, rh + 1
            return node, lh + 1

        return dfs(root)[0]
