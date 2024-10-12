"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return max(range(len(arr)), key=arr.__getitem__)
