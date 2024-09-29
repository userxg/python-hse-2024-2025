"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/remove-k-digits/description/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        if len(num) == k:
            return "0"

        for c in num:
            while stack and stack[-1] > c and k:
                k -= 1
                stack.pop()

            stack.append(c)

        while k:
            k -= 1
            stack.pop()

        if "".join(stack).lstrip("0"):
            return "".join(stack).lstrip("0")
        else:
            return "0"
