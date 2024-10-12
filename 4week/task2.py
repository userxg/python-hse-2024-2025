"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = n - 1, 0

        while i >= 0 and j < m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
