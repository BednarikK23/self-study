# https://leetcode.com/problems/add-two-numbers/submissions/982925946/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
            -> Optional[ListNode]:
        fst, snd = l1, l2
        final = dummy = ListNode(50052)
        carry = 0

        while fst and snd:
            val = fst.val + snd.val
            final.next, carry = ListNode((carry + val) % 10), \
                        (carry + val) // 10

            fst, snd = fst.next, snd.next
            final = final.next

        if fst is None and snd is None:
            if carry != 0:
                final.next = ListNode(1)
            return dummy.next

        if fst is None:
            while snd is not None:
                final.next, carry = ListNode((carry + snd.val) % 10), (
                            carry + snd.val) // 10
                snd, final = snd.next, final.next

        else:
            while fst is not None:
                final.next, carry = ListNode((carry + fst.val) % 10), (
                            carry + fst.val) // 10
                fst, final = fst.next, final.next

        if carry != 0:
            final.next = ListNode(1)

        return dummy.next





