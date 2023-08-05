# https://leetcode.com/problems/palindrome-partitioning/submissions/1012922494/

from typing import List


class Solution:
    def part_rec(self, i: int, s: str, curr: List[str],
                 result: List[List[str]]) -> None:

        if i >= len(s):
            result.append(curr[:])  # in need of copy cause using only 1 curr
            return

        for j in range(i, len(s), 1):
            if s[i:(j + 1)] == ''.join(reversed(s[i:(j + 1)])):
                curr.append(s[i:(j + 1)])
                self.part_rec((j + 1), s, curr, result)
                curr.pop()

    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.part_rec(0, s, [], result)

        return result
