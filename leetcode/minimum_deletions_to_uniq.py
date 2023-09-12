from numpy import Counter

# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/submissions/1047638887/


class Solution:
    def minDeletions(self, s: str) -> int:
        chars = Counter(s)
        frequencies = set()

        deletions = 0
        for ch, f in chars.items():
            while f > 0 and f in frequencies:
                f -= 1
                deletions += 1
            frequencies.add(f)

        return deletions
