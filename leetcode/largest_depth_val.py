# https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/1004430683/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lV_rec(self, curr: TreeNode, depth: int, depths: List[int]) -> None:
        if curr is None:
            return

        if len(depths) <= depth:
            depths.append(curr.val)
        else:
            depths[depth] = max(curr.val, depths[depth])

        self.lV_rec(curr.left, depth + 1, depths)
        self.lV_rec(curr.right, depth + 1, depths)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        depths: List[int] = []
        self.lV_rec(root, 0, depths)

        return depths
