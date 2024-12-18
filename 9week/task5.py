"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-binary-tree-ii/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, node, v: int):

        def fn(root, val):
            if not root or val > root.val:
                new_root = TreeNode(val)
                new_root.left = root
                return new_root

            # Otherwise, recursively insert the value into the right subtree.
            root.right = fn(root.right, val)
            return root

        return fn(node, v)
