# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1026703709/

from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        ch_indxs: Dict[str, int] = {}
        left = 0
        longest = 1

        for right, c in enumerate(s):
            ind = ch_indxs.get(c, -1)

            if ind == -1:
                ch_indxs[c] = right
                continue

            if ind < left:
                ch_indxs[c] = right
            else:
                longest = max(longest, right - left)
                left = ind + 1
                ch_indxs[c] = right

        return max(longest, len(s) - left)
