"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximal-square/description/
"""


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m) for _ in range(n)]

        max_size = 0
        for i in range(n):
            for j in range(m):
                if [i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1])
                max_size = max(dp[i][j], max_size)

        return max_size * max_size
