from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-product-subarray/submissions/1034127440/
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        prev_max = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            curr_max, curr_min = max(num * curr_max, num * curr_min, num), min(num * curr_max, num * curr_min, num)

            prev_max = max(prev_max, curr_max)

        return max(curr_max, prev_max)
