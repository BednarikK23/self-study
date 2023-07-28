# https://leetcode.com/problems/set-matrix-zeroes/submissions/1006122577/
from typing import Set, List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        blank = [0 for _ in range(len(matrix[0]))]
        seen_columns: Set[int] = set()

        for y, row in enumerate(matrix):
            found = False

            for x, elem in enumerate(row):
                if elem == 0:
                    seen_columns.add(x)
                    found = True

            if found:
                matrix[y] = blank.copy()

        for col in seen_columns:
            for r in range(len(matrix)):
                matrix[r][col] = 0
