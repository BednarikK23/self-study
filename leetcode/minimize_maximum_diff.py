# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/submissions/1016607218/
from typing import List


class Solution:
    def smaller_diff(self, nums: List[int], smaller: int, p: int) -> bool:
        count, i = 0, 0

        while i < (len(nums) - 1) and count < p:
            if nums[i + 1] - nums[i] <= smaller:
                i += 1
                count += 1
            i += 1

        return count == p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        if len(nums) == 2:  # p have to be 1
            return abs(nums[0] - nums[1])

        nums.sort()

        bot, top = 0, nums[-1] - nums[0]  # limits, try to get teneser
        while bot < top:
            mid = bot + (top - bot) // 2

            if not self.smaller_diff(nums, mid, p):
                bot = mid + 1
                continue

            top = mid

        return bot


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimizeMax([3, 4, 2, 3, 2, 1, 2], 3) == 1
