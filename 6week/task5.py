"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = nums.count(1)
        c = nums[:n].count(1)
        mc = c
        nums += nums[: n - 1]

        for i in range(1, len(nums) - n + 1):
            c += nums[i + n - 1] - nums[i - 1]
            mc = max(mc, c)

        return n - mc
