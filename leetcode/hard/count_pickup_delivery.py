# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/submissions/1045618162/

class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for curr in range(2, n * 2 + 1, 2):
            valid = (curr * (curr - 1)) // 2
            res *= valid

        return res % (10**9 + 7)
