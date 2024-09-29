"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/number-of-matching-subsequences/description/
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:

        def is_sub(word: str) -> bool:
            idx = -1
            for ch in word:
                idx = s.find(ch, idx + 1)
                if idx == -1:
                    return False
            return True

        k = 0
        for word in words:
            if (is_sub(word)) is True:
                k += 1

        return k
