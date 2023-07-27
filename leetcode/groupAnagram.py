# https://leetcode.com/problems/group-anagrams/submissions/1005312157/
from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: Dict[str, List[str]] = {}

        for s in strs:
            # if not .join() its treated like a list - could not be
            # used in dict, cause mutable
            word = "".join(sorted(s))
            l = result.get(word)

            if l is None:
                result[word] = [s]
            else:
                l.append(s)

        return list(result.values())
