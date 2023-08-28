from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/reverse-linked-list/submissions/1033935514/
        if head is None:
            return None

        curr, nxt = head, head.next
        curr.next = None
        while nxt is not None:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        return curr

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == 4:
            return 2

        top = x // 2
        bot = 2
        while bot <= top:
            mid = bot + (top - bot) // 2

            m = mid * mid
            if m == x:
                return mid

            if m < x:
                bot = mid + 1
            else:
                top = mid - 1

        return top

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n, x = -n, 1 / x

        ans = 1
        for i in range(n.bit_length() - 1, -1, -1):
            ans *= ans
            if n & (1 << i):
                ans *= x

        return ans

