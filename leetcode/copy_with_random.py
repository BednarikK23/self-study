from typing import Optional, Dict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1041515170/
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        if head is None:
            return None

        news: Dict[Node, Node] = {}

        curr = head
        while curr is not None:
            news[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr is not None:
            news[curr].next = news.get(curr.next)
            news[curr].random = news.get(curr.random)
            curr = curr.next

        return news[head]
