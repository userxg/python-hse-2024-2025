"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_ar = s.split()[::-1]
        return " ".join(s_ar)
