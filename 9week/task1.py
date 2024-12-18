"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

from collections import deque


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels
