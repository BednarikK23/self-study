from typing import Optional, List


# https://leetcode.com/problems/split-linked-list-in-parts/submissions/1042072116/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) \
            -> List[Optional[ListNode]]:
        if head is None:
            return [None for _ in range(k)]

        length, node = 0, head
        while node is not None:
            length += 1
            node = node.next

        lls: List[Optional[ListNode]] = []
        node = head
        for i in range(k):
            l = length // k
            l += 1 if i < length % k else 0
            lls.append(node)

            for j in range(l):
                if j + 1 == l:
                    prev = node
                    node = node.next
                    prev.next = None
                else:
                    node = node.next

        return lls
