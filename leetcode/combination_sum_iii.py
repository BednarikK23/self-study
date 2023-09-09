from typing import List

# https://leetcode.com/problems/combination-sum-iii/submissions/1044691971/


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result: List[List[int]] = []

        def rec(curr: List[int], curr_sum: int, curr_i: int) -> None:
            if len(curr) >= k:
                return

            for num in range(curr_i, 10):
                s = num + curr_sum
                if s == n:
                    if len(curr) + 1 < k:
                        return
                    curr.append(num)
                    result.append(curr[:])
                    curr.pop()
                    return

                if s > n:
                    return

                curr.append(num)
                rec(curr, s, num + 1)
                curr.pop()

        rec([], 0, 1)
        return result
