"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ["a", "b", "c"]:
                stack.pop()
                stack.pop()
                stack.pop()

        if len(stack) == 0:
            return True

        return False
