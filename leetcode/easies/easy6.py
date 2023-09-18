from typing import Optional, List


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

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/1052776864/
        def count(i):
            c = 0
            for elem in mat[i]:
                if elem == 0:
                    return c
                c += 1
            return c

        evaluated = [(count(i), i) for i in range(len(mat))]
        evaluated.sort()

        res = []
        j = 0
        for i, indx in evaluated:
            if k == j:
                return res
            res.append(indx)
            j += 1
        return res

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

    # https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1040684238/
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev, node = head, head.next
        while node is not None:
            if prev.val == node.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return head

    def generate(self, numRows: int) -> List[List[int]]:
        # https://leetcode.com/problems/pascals-triangle/submissions/1043723387/
        res = [[1]]

        def get(arr: List[int], index: int) -> int:
            if index - 1 < 0:
                return arr[index]
            if index >= len(arr):
                return arr[index - 1]

            return arr[index - 1] + arr[index]

        for i in range(2, numRows + 1):
            new = []

            for j in range(i):
                new.append(get(res[-1], j))

            res.append(new)

        return res
