# https://leetcode.com/problems/find-bottom-left-tree-value/submissions/1004404151/
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def fBLV_rec(self, curr: TreeNode, depth: int) -> Tuple[
        int, int]:  # depth, val
        if curr.left is None and curr.right is None:
            return depth, curr.val

        if curr.left is not None and curr.right is not None:
            d_l, v_l = self.fBLV_rec(curr.left, depth + 1)
            d_r, v_r = self.fBLV_rec(curr.right, depth + 1)

            if d_l == d_r:
                return d_l, v_l
            return max((d_l, v_l), (d_r, v_r))

        if curr.left is None:
            return self.fBLV_rec(curr.right, depth + 1)

        return self.fBLV_rec(curr.left, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        _, result = self.fBLV_rec(root, 0)
        return result
