from typing import List

# https://leetcode.com/problems/candy/submissions/1048216743/


class Solution:
    def candy(self, ratings: List[int]) -> int:
        amounts = [1 for _ in range(len(ratings))]
        def get(i):
            if i < 0:
                return amounts[0]
            if i >= len(amounts):
                return amounts[-1]
            return amounts[i]

        prev = ratings[0]
        for i, curr in enumerate(ratings):
            if curr > prev:
                amounts[i] = get(i - 1) + 1
            prev = curr

        result = amounts[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                amounts[i] = max(amounts[i], get(i + 1) + 1)
            result += amounts[i]

        return result
