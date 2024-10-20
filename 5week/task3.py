"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams/description/
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())
