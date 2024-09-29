"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/generate-parentheses/description/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n -= 1
        result = {"()"}

        while n > 0:
            newResult = set()
            for item in result:
                for i in range(len(item)):
                    newResult.add(item[:i] + "()" + item[i:])
            result = newResult
            n -= 1
        return result
