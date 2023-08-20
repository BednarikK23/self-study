# again, if the easy exercises aren't too long I ll not create special file for
# them and just place them here...

from typing import List, Optional, Tuple

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1026680063/
        if prices == []:
            return 0

        left, min_price = 0, prices[0]
        best = 0
        for right, price in enumerate(prices):
            if price < min_price:
                left = right
                min_price = price
                continue

            curr_profit = price - min_price
            if curr_profit > best:
                best = curr_profit

        return best
