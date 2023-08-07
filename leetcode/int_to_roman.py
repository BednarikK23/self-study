# https://leetcode.com/problems/integer-to-roman/submissions/1014545519/

class Solution:
    D = {
        1 : "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
        10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
        100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
        1000: "M", 2000: "MM", 3000: "MMM"
        }

    def intToRoman(self, num: int) -> str:
        modulers = [10, 100, 1_000, 10_000]
        result = []

        x = 0
        while num > 0 and x < 4:
            curr = num % modulers[x]
            if curr == 0:
                x += 1
                continue
            result.append(self.D[curr])
            num -= curr
            x += 1

        return "".join(reversed(result))
