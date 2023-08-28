from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-subarray/submissions/1033994095/
        curr, res = nums[0], nums[0]
        cont = False

        for num in nums:
            if not cont:
                cont = True
                continue

            prev, curr = curr, curr + num
            if prev > res:
                res = prev
            if prev < 0:
                curr = num

        return max(res, curr)
