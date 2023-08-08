# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1015802426/
# i just found out there are daily challenges on leetcode, so even tho
# i have no time i did something, its nobrainer but i ve done first daily challange... xD

from typing import List, Tuple
from random import randint


class Solution:
    def find_pivot_or_luck(self, nums: List[int], target: int, l: int,
                           r: int, _fst: int) -> Tuple[int, bool]:
        while l < r:
            mid = l + (r - l) // 2
            curr = nums[mid]

            if curr == target:
                return mid, True

            if curr > _fst:
                if mid + 1 < len(nums) and nums[mid + 1] < _fst:
                    return mid + 1, (nums[mid + 1] == target)
                l = mid + 1

            else:  # curr <= _fst
                if mid - 1 > 0 and nums[mid - 1] > _fst:
                    return mid, (nums[mid - 1] == target)
                r = mid - 1

        return r, False

    def find(self, nums: List[int], target: int, l: int, r: int):
        if l > r or 0 > r or len(nums) <= l:
            return -1

        if l == r:
            return -1 if nums[l] != target else l

        mid = l + (r - l) // 2
        curr = nums[mid]

        if curr == target:
            return mid

        if curr < target:
            return self.find(nums, target, mid + 1, r)

        return self.find(nums, target, l, mid)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 10:
            for i, num in enumerate(nums):
                if num == target:
                    return i
            return -1

        indx, luck = self.find_pivot_or_luck(nums, target, 0, len(nums), nums[0])
        if luck:
            return indx

        if target < nums[0]:
            return self.find(nums, target, indx + 1, len(nums))
        return self.find(nums, target, 0, indx)


if __name__ == '__main__':
    s = Solution()
    arr = [i for i in range(8, 50)]
    arr.extend([i for i in range(-20, 8)])

    for _ in range(100):
        r = randint(-50, 100)
        res = s.search(arr, r)
        print(r)

        if -20 <= r < 50:
            assert  != -1
        else:
            assert s.search(arr, r) == -1

