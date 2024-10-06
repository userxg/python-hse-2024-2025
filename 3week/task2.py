"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ind1 = 0
        ind2 = len(numbers) - 1
        while ind1 < ind2:
            if (numbers[ind1] + numbers[ind2]) < target:
                ind1 += 1
            if (numbers[ind1] + numbers[ind2]) > target:
                ind2 -= 1
            if (numbers[ind1] + numbers[ind2]) == target:
                return [ind1 + 1, ind2 + 1]
