class Solution:
    # https://leetcode.com/problems/unique-paths/submissions/1039310530/
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]

        for _ in range(m - 1):
            new = [1 for _ in range(n)]

            for j in range(n - 2, -1, -1):
                new[j] = new[j + 1] + row[j]
            row = new

        return row[0]

    # https://leetcode.com/problems/unique-paths/submissions/1039299262/
    def uniquePaths2(self, m: int, n: int) -> int:
        memos = [{n: 0} for _ in range(m)]
        memos[m - 1][n - 1] = 1

        def dfs(x, y):
            if x >= m:
                return 0

            if y in memos[x]:
                return memos[x][y]

            curr = dfs(x + 1, y) + dfs(x, y + 1)
            memos[x][y] = curr
            return curr

        return dfs(0, 0)
