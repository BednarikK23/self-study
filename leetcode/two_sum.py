#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


from math import inf
from typing import List


class Solution:
    # complexity O(n+n+n*log(n)) -> O(n*log(n))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sns = sorted(nums)  # O(n*log(n))

        l, r = 0, len(sns) - 1
        final_nums = 0, 0

        while l < r:  # O(n)
            s = sns[l] + sns[r]
            if s == target:
                final_nums = sns[l], sns[r]
                break
            if s < target:
                l += 1
            if s > target:
                r -= 1

        result = []
        for i, num in enumerate(nums):  # O(n)
            fst, snd = final_nums
            if num == fst:
                finial_nums = inf, snd
                result.append(i)
                continue

            if num == snd:
                finial_nums = fst, inf
                result.append(i)

            if len(result) == 2:
                break

        return result