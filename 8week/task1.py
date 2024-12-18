"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        start = 0
        end = 0
        n = len(arr)
        count = 0
        avg = 0
        sum = 0
        while end < n:
            if k > (end - start):
                sum += arr[end]
            if k == (end - start + 1):
                avg = sum / float(k)
                if avg >= threshold:
                    count += 1
                sum -= arr[start]
                start += 1
            end += 1

        return count
