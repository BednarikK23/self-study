# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1015571694/
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {num: i for i, num in enumerate(inorder)}
        preord_indx = 0

        _, res = self.rec(0, len(preorder) - 1, preord_indx, preorder, indexes)
        return res

    def rec(self, l: int, r: int, index: int, preorder: List[int], indexes: Dict[int, int]) -> Optional[Tuple[int, TreeNode]]:
        if l > r:
            return index, None

        curr = TreeNode(preorder[index])
        index += 1

        i = indexes[curr.val]

        index, curr.left = self.rec(l, i - 1, index, preorder, indexes)
        index, curr.right = self.rec(i + 1, r, index, preorder, indexes)

        return index, curr
