from math import factorial
from typing import Dict, List


class Solution:
    def cal(self, d: Dict[int, int], num: int):
        c = d.get(num, 0)
        d[num] = c + 1

        res = 1
        for n in d.values():
            if n == 0:
                continue
            res *= factorial(n)

        d[num] -= 1
        return res

    def combinationSum4(self, nums: List[int], target: int) -> int:

        def rec(d: Dict[int, int], length: int, curr_sum: int, curr_i: int,
                result: int) -> int:
            for i in range(curr_i, len(nums)):
                num = nums[i]
                s = num + curr_sum

                if s > target:
                    return result

                if s == target:
                    return result + (factorial(length + 1) // self.cal(d, num))

                c = d.get(num, 0)
                d[num] = c + 1
                result = rec(d, length + 1, s, i, result)
                d[num] -= 1

            return result

        nums.sort()
        return rec({}, 0, 0, 0, 0)
