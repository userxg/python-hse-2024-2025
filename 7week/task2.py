"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        sum_left, sum_right = sum(cardPoints[:k]), 0
        res = sum_left
        for i in range(k):
            sum_left -= cardPoints[k - 1 - i]
            sum_right += cardPoints[len(cardPoints) - 1 - i]
            res = max(res, sum_left + sum_right)
        return res
