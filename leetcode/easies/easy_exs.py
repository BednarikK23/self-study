from typing import List, Optional, Tuple, Set


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        # https://leetcode.com/problems/add-binary/submissions/1012067506/
        result = []
        counter, i = 0, 1

        for i in range(1, min(len(a), len(b)) + 1):
            if a[-i] == '1':
                counter += 1
            if b[-i] == '1':
                counter += 1

            result.append(str(counter % 2))

            counter = 1 if counter >= 2 else 0
        i += 1

        while i <= len(a):
            counter += 1 if a[-i] == '1' else 0
            result.append(str(counter % 2))
            counter = 1 if counter > 1 else 0
            i += 1

        while i <= len(b):
            counter += 1 if b[-i] == '1' else 0
            result.append(str(counter % 2))
            counter = 1 if counter > 1 else 0
            i += 1

        if counter > 0:
            result.append('1')

        return "".join(reversed(result))


    def lengthOfLastWord(self, s: str) -> int:
        # https://leetcode.com/problems/length-of-last-word/submissions/1011932408/
        words = s.split()
        return 0 if not words else len(words[-1])

    def isPalindrome(self, x: int) -> bool:
        # https://leetcode.com/problems/palindrome-number/submissions/1026127777/
        if x == 0:
            return True

        if x < 0 or x % 10 == 0:
            return False

        new, old = 0, x
        while old > new:
            new *= 10
            new += old % 10
            old //= 10

        return old == new or old == new // 10

    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        # https://leetcode.com/problems/roman-to-integer/submissions/1026135692/
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        res = 0
        for c in s:
            res += self.numbers[c]

        return res
