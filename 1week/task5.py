"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        dict = [
            [1, "I"],
            [4, "IV"],
            [5, "V"],
            [9, "IX"],
            [10, "X"],
            [40, "XL"],
            [50, "L"],
            [90, "XC"],
            [100, "C"],
            [400, "CD"],
            [500, "D"],
            [900, "CM"],
            [1000, "M"],
        ]

        i = 12

        while num > 0:
            if num >= dict[i][0]:
                res += dict[i][1]
                num -= dict[i][0]
            else:
                i -= 1
        return res
