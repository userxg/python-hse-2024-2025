"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/path-sum-ii/description/
"""


class Solution:
    def dfs(self, root, path, ans, remainingSum):

        if not root:
            return

        path.append(root.val)

        if not root.left and not root.right and remainingSum == root.val:
            ans.append(list(path))

        self.dfs(root.left, path, ans, remainingSum - root.val)
        self.dfs(root.right, path, ans, remainingSum - root.val)

        path.pop()

    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        ans = []
        self.dfs(root, [], ans, targetSum)
        return ans
