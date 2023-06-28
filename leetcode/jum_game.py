# https://leetcode.com/problems/jump-game-ii/submissions/981665441/
#
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        curr, index = nums[0], 0
        jumps = 1

        while curr < len(nums) - 1:
            start, stop = index + 1, curr + 1
            for i in range(start, stop):
                if curr < i + nums[i]:
                    curr = i + nums[i]
                    index = i

            jumps += 1

        return jumps















