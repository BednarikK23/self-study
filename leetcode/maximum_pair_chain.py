# https://leetcode.com/problems/maximum-length-of-pair-chain/submissions/1032580489/

from typing import Tuple, List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0

        def sorting_foo(x: Tuple[int, int]) -> int:
            _, res = x
            return res

        pairs.sort(key=sorting_foo)
        curr, res = pairs[0][0] - 1, 0

        for fst, snd in pairs:
            if fst > curr:
                curr = snd
                res += 1

        return res
