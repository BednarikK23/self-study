from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # https://leetcode.com/problems/linked-list-cycle/submissions/1034198533/
        slow = fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False

    def rec(self, n, mem):
        if n in mem:
            return mem[n]

        mem[n] = n % 2 + self.rec(n // 2, mem)
        return mem[n]

    # https://leetcode.com/problems/counting-bits/submissions/1037982342/
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mem = {0: 0, 1: 1}
        return [self.rec(i, mem) for i in range(n + 1)]
