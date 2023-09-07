from typing import Optional

# https://leetcode.com/problems/reverse-linked-list-ii/submissions/1042961363/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int,
                       right: int) -> Optional[ListNode]:
        if head is None or left >= right:
            return head

        dummy = node = ListNode(0, head)
        prev_l, l, r = dummy, None, None
        counter = 0

        while node is not None and counter <= right:
            if counter + 1 == left:
                prev_l = node
            if counter == left:
                l = node
            if counter == right:
                r = node
            counter += 1
            node = node.next

        prev_l.next = r
        curr = l
        while curr != r:
            rnxt = r.next
            r.next = curr
            prev = curr
            curr = curr.next
            prev.next = rnxt

        return dummy.next
