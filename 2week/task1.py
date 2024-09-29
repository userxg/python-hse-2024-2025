"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/compare-version-numbers/description/
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        version1 = [int(x) for x in version1]
        version2 = [int(x) for x in version2]
        idx = 0
        while idx < len(version1) and idx < len(version2):
            if version1[idx] == version2[idx]:
                idx += 1
                continue
            if version1[idx] < version2[idx]:
                return -1
            else:
                return 1

        while idx < len(version1):
            if version1[idx]:
                return 1
            idx += 1
        while idx < len(version2):
            if version2[idx]:
                return -1
            idx += 1
        return 0
