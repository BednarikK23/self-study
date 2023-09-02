from typing import Dict, List

# https://leetcode.com/problems/extra-characters-in-a-string/submissions/1038414098/


class TrieNode:
    def __init__(self) -> None:
        self.chars: Dict[str, 'TrieNode'] = {}
        self.end = False


class Trie:
    def __init__(self, words: List[str]) -> None:
        self.root = TrieNode()

        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.chars:
                    curr.chars[c] = TrieNode()
                curr = curr.chars[c]
            curr.end = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        memo = {len(s): 0}

        def dfs(i):
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)  # either skip

            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.chars:
                    memo[i] = res
                    return res

                curr = curr.chars[s[j]]

                if curr.end:
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)
