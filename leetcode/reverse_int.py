class Solution:
    # https://leetcode.com/problems/reverse-integer/submissions/1043795044/
    def reverse(self, x: int) -> int:
        new = 0
        old = x if x >= 0 else -x
        while old != 0:
            new = new * 10 + old % 10
            old //= 10

        if new > (2 ** 31 - 1) or (new < -2 ** 31):
            return 0
        return new if x >= 0 else -new
