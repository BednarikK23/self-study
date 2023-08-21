from typing import List

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
