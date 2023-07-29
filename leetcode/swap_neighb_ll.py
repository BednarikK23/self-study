# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1006819934/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = last = ListNode()
        last.next = head
        curr = head

        while curr is not None and curr.next is not None:
            last.next = curr.next
            tmp = curr.next

            curr.next = tmp.next
            tmp.next = curr

            last = curr
            curr = curr.next

        return dummy.next
