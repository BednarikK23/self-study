from typing import Optional
from timeit import default_timer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __int__(self):
        pass

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ \
        ListNode]:
        if head is None:
            return head

        dummy = ListNode(x, head)
        curr, lst_small, lst_big = head, dummy, dummy
        while curr is not None:
            if curr.val < x:
                if curr is lst_small.next:
                    lst_small = lst_big = curr
                    curr = curr.next
                    continue

                fst_big = lst_small.next

                lst_small.next = curr
                lst_big.next = curr.next
                curr.next = fst_big

                lst_small = curr
                curr = lst_big
            else:
                lst_big = curr

            curr = curr.next

        return dummy.next

    def snd(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small = ListNode(0)
        dummy_big = ListNode(1)


        curr, lst_small, lst_big = head, dummy_small, dummy_big
        while curr is not None:
            if curr.val < x:
                lst_small.next = curr
                lst_small = curr
            else:
                lst_big.next = curr
                lst_big = curr
            curr = curr.next

        lst_small.next = dummy_big.next
        lst_big.next = None

        return dummy_small.next


if __name__ == '__main__':
    sol = Solution()

    head = ListNode(1, ListNode(4,
            ListNode(3, ListNode(0,
             ListNode(2, ListNode(5, ListNode(2)))))))

    one = default_timer()
    result = node = sol.partition(head, 3)
    two = default_timer()

    while node is not None:
        print(node.val, "->", end=" ")
        node = node.next
    print("")


    head = ListNode(1, ListNode(4,
            ListNode(3, ListNode(0,
             ListNode(2, ListNode(5, ListNode(2)))))))

    three = default_timer()
    result = node = sol.snd(head, 3)
    four = default_timer()

    while node is not None:
        print(node.val, "->", end=" ")
        node = node.next
    print()
    adin, dva = two - one, four - three
    print(adin, " vs ", dva, "=", adin > dva)

