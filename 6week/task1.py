"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/description/
"""


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # use two mid pointes method
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # mid + k must not out of range
            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                left = mid + 1
            # if All duplicate and the first one is large than x
            # arr[mid] < x need to filter out this kind of case: [1,1,2,2,2,2,2,2,2,2] 3 1
            elif arr[mid] == arr[mid + k] and arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]
