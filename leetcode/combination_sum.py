from typing import List

# https://leetcode.com/problems/combination-sum/submissions/1044631568/


class Solution:
    def rec(self, candidates: List[int], curr: List[int], curr_sum: int,
            result: List[List[int]], target: int, index: int) -> None:
        for i in range(index, len(candidates)):
            num = candidates[i]
            if curr_sum + num > target:
                continue

            curr.append(num)

            if curr_sum + num == target:
                result.append(curr[:])
                curr.pop()
                continue

            self.rec(candidates, curr, curr_sum + num, result, target, i)
            curr.pop()

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        result: List[List[int]] = []
        self.rec(candidates, [], 0, result, target, 0)

        return result
