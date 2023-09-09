from typing import List

# https://leetcode.com/problems/combination-sum-ii/submissions/1044662749/


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        result: List[List[int]] = []
        candidates.sort()

        def rec(curr: List[int], index: int, curr_sum: int) -> None:
            if target < curr_sum:
                return

            if target == curr_sum:
                result.append(curr[:])
                return

            # important to have prev because it is set after the recursion...
            prev = candidates[0] - 1
            for i in range(index, len(candidates)):
                num = candidates[i]
                if i > 0 and num == prev:
                    continue

                curr.append(num)
                rec(curr, i + 1, curr_sum + num)
                curr.pop()
                prev = num

        rec([], 0, 0)
        return result
