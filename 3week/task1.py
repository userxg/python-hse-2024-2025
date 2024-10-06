"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        x = prices[0]
        for i in range(1, len(prices)):
            if x > prices[i]:
                x = prices[i]
            else:
                res += prices[i] - x
                x = prices[i]
        return res
