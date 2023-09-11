from typing import List, Dict

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/1046322118/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        sizes_groups: Dict[int, List[int]] = {}

        for i, num in enumerate(groupSizes):
            a = sizes_groups.get(num, [])
            a.append(i)

            if len(a) == num:
                result.append(a)
                a = []

            sizes_groups[num] = a

        return result
