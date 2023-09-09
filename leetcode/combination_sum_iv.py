from typing import List

# https://leetcode.com/problems/combination-sum-iv/submissions/1044741135/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {0: 1}
        for t in range(1, target + 1):
            for n in nums:
                mem[t] = mem.get(t, 0) + mem.get(t - n, 0)

        return mem[target]