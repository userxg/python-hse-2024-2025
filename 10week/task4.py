"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
"""


class Solution:
    def minimumOperations(self, root) -> int:
        ans, queue, level = 0, [root], []
        while queue:
            for node in queue:
                if node:
                    level.extend([node.left, node.right])
            arr = [(v, i) for i, v in enumerate([c.val for c in level if c])]
            idx = [i for _, i in sorted(arr)]
            for i in range(len(idx)):
                while idx[i] != i:
                    j = idx[i]
                    idx[i], idx[j] = idx[j], idx[i]
                    ans += 1

            queue, level = level, []

        return ans
