# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/submissions/1017423541/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) < 10:
            for num in nums:
                if num == target:
                    return True
            return False

        low, high = 0, len(nums) - 1

        while low <= high:
            if high == low:
                return nums[low] == target

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
            # redundancy of elems is problem for  basic solution, so need
            # to add this inefficient but necessary...
            if nums[low] == nums[mid]:
                low += 1
                if nums[low] == target:
                    return True
                continue

            # 1. find out which half is sorted
            # so we can compare if the element is in
            # that part if not go the other way...

            if nums[mid] < nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
