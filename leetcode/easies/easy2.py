# again, if the easy exercises aren't too long I ll not create special file for
# them and just place them here...

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # https://leetcode.com/problems/longest-common-prefix/submissions/1027521144/
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            for s in strs:
                if len(s) <= i or s[i] != char:
                    return s[:i]

        return strs[0]

    def isValid(self, s: str) -> bool:
        # https://leetcode.com/problems/valid-parentheses/submissions/1027540422/
        stack: List[int] = []
        brackets = {')': 1, '(': 2, ']': 3, '[': 4, '}': 5, '{': 6}

        for c in s:
            curr = brackets.get(c, 0)

            if curr == 0:
                return False  # not possible

            if curr % 2 == 0:
                stack.append(curr)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != curr + 1:
                    return False

        return len(stack) == 0

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/merge-two-sorted-lists/submissions/1027546379/
        n, m = list1, list2
        res = dummy = ListNode()

        while n is not None and m is not None:
            if n.val <= m.val:
                res.next = n
                res = n
                n = n.next
            else:
                res.next = m
                res = m
                m = m.next

        if n is None:
            res.next = m
        else:
            res.next = n

        return dummy.next


