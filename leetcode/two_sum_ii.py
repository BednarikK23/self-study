from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1034021229/
        if len(numbers) < 2:
            return []

        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
        return []
