# https://leetcode.com/problems/search-a-2d-matrix/submissions/1015857463/
from typing import List
LUCK = -69


class Solution:
    def find_row(self, matrix: List[List[int]], target: int) -> int:
        l, r = 0, len(matrix)
        while l < r:
            mid = l + (r - l) // 2
            curr_l, curr_r = matrix[mid][0], matrix[mid][-1]

            if curr_l == target or curr_r == target:
                return LUCK

            if target < curr_l:
                r = mid - 1
                continue

            if target > curr_r:
                l = mid + 1
                continue

            return mid

        if l == r:
            if r < len(matrix):
                if matrix[r][0] == target or matrix[r][-1] == target:
                    return LUCK
                return r if matrix[r][0] <= target <= matrix[r][-1] else -1

        return -1

    def find_num(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1

        while l < r:
            mid = l + (r - l) // 2
            curr = row[mid]

            if curr == target:
                return True
            if target < curr:
                r = mid - 1
            if target > curr:
                l = mid + 1

        return l == r and row[l] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        i = self.find_row(matrix, target)
        if i == -1:
            return False
        if i == LUCK:
            return True

        row = matrix[i]

        return self.find_num(row, target)


if __name__ == '__main__':
    sol = Solution()

    a = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]]
    assert sol.searchMatrix(a, 3)
    for row in a:
        for num in row:
            assert sol.searchMatrix(a, num)

    for num in [-1, -20, 8, 9, 12, 6, 4, 18, 21, 22,
                24, 31, 36, 40, 50, 70, 1000]:
        assert not sol.searchMatrix(a, num)
