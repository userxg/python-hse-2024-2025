"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/sliding-window-maximum/description/
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        q = deque()

        for ind, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if ind >= k and nums[ind - k] == q[0]:
                q.popleft()

            if ind >= k - 1:
                ans.append(q[0])

        return ans
