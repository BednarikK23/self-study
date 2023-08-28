from typing import List


class MyStack:
    # https://leetcode.com/problems/implement-stack-using-queues/submissions/1033890392/
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack == []:
            return 0
        return self.stack.pop()

    def top(self) -> int:
        if self.stack == []:
            return 0
        return self.stack[-1]

    def empty(self) -> bool:
        return self.stack == []


class Solution:
    f, b, fb = "Fizz", "Buzz", "FizzBuzz"

    def fizzBuzz(self, n: int) -> List[str]:
        # https://leetcode.com/problems/fizz-buzz/submissions/1027506508/
        res = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append(self.fb)
                continue
            if i % 3 == 0:
                res.append(self.f)
                continue
            if i % 5 == 0:
                res.append(self.b)
                continue
            res.append(str(i))

        return res

    def singleNumber(self, nums):
        # https://leetcode.com/problems/single-number/submissions/1034307431/
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        l, r = 1, len(nums) - 2
        while l <= r:
            m = l + (r - l) // 2
            if nums[m - 1] != nums[m] != nums[m + 1]:
                return nums[m]
            if m % 2 == 0:
                m -= 1

            if nums[m - 1] != nums[m] != nums[m + 1]:
                return nums[m]
            if nums[m] != nums[m - 1]:  # after single
                r = m - 1
            else:
                l = m + 1

        return 0
