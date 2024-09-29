"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digit_str: str) -> list[str]:
        if len(digit_str) == 0:
            return []

        digit_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def recurComb(idx, comb):
            if idx == len(digit_str):
                res.append(comb)
                return

            for letter in digit_dict[digit_str[idx]]:
                recurComb(idx + 1, comb + letter)

        recurComb(0, "")

        return res
