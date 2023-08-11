from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coin_ways = [0 for _ in range(amount + 1)]
        coin_ways[0] = 1  # only one way how to get nothing - nothing

        # this is damn cool trick...
        # in coin_ways - each index represents value and element of that index
        # represent how many ways we can get to this value with our coins...
        # if we have coin of certain value we increment counter of element of
        # that index
        # and every other element that has been affected by this change...
        # it takes care about how many ways we could get to the number
        # before and then cumulates it
        for coin in coins:
            if coin > amount:
                continue
            # coin_ways[j] += 1  //  for loop will take care of that if u
            # think about it...
            for j in range(coin, amount + 1):
                coin_ways[j] += coin_ways[j - coin]

        # we can find the result on the last index...
        return coin_ways[amount]
