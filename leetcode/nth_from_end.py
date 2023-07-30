# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1007932743/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(0, head)

        self.recc(dummy, n)

        return dummy.next

    def recc(self, curr: ListNode, n: int) -> int:
        if curr is None:
            return 1

        x = self.recc(curr.next, n)

        if x == n + 1 and curr.next is not None:
            curr.next = curr.next.next

        return x + 1
