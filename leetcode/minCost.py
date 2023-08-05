# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/submissions/1012730206/
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        counter = 1
        sum_same = neededTime[0]
        max_same = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                counter += 1
                sum_same += neededTime[i]
                max_same = max(max_same, neededTime[i])
                continue

            if counter > 1:
                result += (sum_same - max_same)

            counter = 1
            sum_same = neededTime[i]
            max_same = neededTime[i]

        if counter > 1:
            result += (sum_same - max_same)

        return result
