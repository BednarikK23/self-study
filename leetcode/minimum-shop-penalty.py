class Solution:
    # https://leetcode.com/problems/minimum-penalty-for-a-shop/submissions/1034988657/
    def bestClosingTime(self, customers: str) -> int:
        came, didnt = 0, 0
        for c in customers:
            if c == 'N':
                didnt += 1
            else:
                came += 1

        best_closing = came - didnt
        closing_time = 0
        for i, c in enumerate(customers):
            if c == 'Y':
                came -= 1
            else:
                didnt -= 1

            curr = came - didnt
            if curr < best_closing:
                best_closing = curr
                closing_time = i + 1

        return closing_time
