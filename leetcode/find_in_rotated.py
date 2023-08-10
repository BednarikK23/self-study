# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1017429742/
# i just found out there are daily challenges on leetcode

from typing import List, Tuple
from random import randint


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 10:
            for i, num in enumerate(nums):
                if num == target:
                    return i

            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            if high == low:
                return low if nums[low] == target else -1

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
            # redundancy of elems is problem for  basic solution, so need
            # to add this inefficient but necessary...
            if nums[low] == nums[mid]:
                low += 1
                if nums[low] == target:
                    return low
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

        return -1


if __name__ == '__main__':
    s = Solution()
    arr = [i for i in range(8, 50)]
    arr.extend([i for i in range(-20, 8)])

    for _ in range(100):
        r = randint(-50, 100)
        res = s.search(arr, r)
        print(r)

        if -20 <= r < 50:
            assert res != -1
        else:
            assert res == -1

