"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
"""


class Solution:
    def maximumSubarraySum(self, nums, k):
        s = set()
        n = len(nums)
        sum_ = 0
        mx = 0
        j = 0

        for i in range(n):
            while nums[i] in s:
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1

            s.add(nums[i])
            sum_ += nums[i]

            if len(s) == k:
                mx = max(mx, sum_)
                sum_ -= nums[j]
                s.remove(nums[j])
                j += 1

        return mx
