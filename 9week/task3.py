"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
"""

from collections import deque


class Solution:
    def isCompleteTree(self, root) -> bool:

        if not root:
            return True

        q = deque([root])

        while q[0] is not None:

            node = q.popleft()

            q.append(node.left)
            q.append(node.right)

        while q and q[0] is None:
            q.popleft()
