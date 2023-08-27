# https://leetcode.com/problems/frog-jump/submissions/1033055991/

from typing import List, Dict, Set


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[0] != 0 or stones[1] != 1:
            return False

        memo: Dict[int, Set[int]] = {s: set() for s in stones}
        memo[0].add(0)

        for i in range(len(stones)):
            for k in memo[stones[i]]:
                for step in range(k-1, k+2):
                    next_jump = stones[i] + step
                    if step and next_jump in memo:
                        memo[next_jump].add(step)

                if len(memo[stones[-1]]) > 0:
                    return True

        return False
