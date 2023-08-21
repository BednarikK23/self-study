from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1027561860/
        if nums == []: return 0

        unique, previous = 1, nums[0]

        for i, num in enumerate(nums):
            if num != previous:
                previous = nums[unique] = num
                unique += 1

        return unique

    def removeElement(self, nums: List[int], val: int) -> int:
        # https://leetcode.com/problems/remove-element/submissions/1027578146/
        if nums == []:
            return 0

        unvalid = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[- 1 - unvalid]
                unvalid += 1

        return len(nums) - unvalid

    def plusOne(self, digits: List[int]) -> List[int]:
        # https://leetcode.com/problems/plus-one/submissions/1027756110/
        rest = 1
        for i in range(len(digits) - 1, -1, -1):
            rest, digits[i] = (digits[i] + 1) // 10, (digits[i] + 1) % 10
            if rest == 0:
                return digits

        if rest == 1:
            digits.insert(0, 1)
        return digits

    def countSegments(self, s: str) -> int:
        # https://leetcode.com/problems/number-of-segments-in-a-string/submissions/1027480924/
        return len(s.split())

    def repeatedSubstringPattern(self, s: str) -> bool:
        # https://leetcode.com/problems/repeated-substring-pattern/submissions/1027465372/
        l = len(s)

        for i in range(l // 2, 0, -1):
            if l % i == 0:
                if (s[:i] * (l // i)) == s:
                    return True

        return False

