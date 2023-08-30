from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-replacements-to-sort-the-array/submissions/1035781548/
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        for i in range(2, len(nums) + 1):
            curr, prev = nums[-i], nums[-i+1]
            if curr <= prev:
                continue

            if curr % prev == 0:
                steps = curr // prev
            else:
                steps = curr // prev + 1
            nums[-i] = curr // steps
            res += steps - 1

        return res
