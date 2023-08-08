# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1015592177/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexes = {num: i for i, num in enumerate(inorder)}
        postord_indx = len(postorder) - 1

        _, res = self.rec(0, len(postorder) - 1, postord_indx, postorder, indexes)
        return res

    def rec(self, l: int, r: int, index: int, postorder: List[int], indexes: Dict[int, int]) -> Optional[Tuple[int, TreeNode]]:
        if l > r:
            return index, None

        curr = TreeNode(postorder[index])
        index -= 1

        i = indexes[curr.val]

        index, curr.right = self.rec(i + 1, r, index, postorder, indexes)
        index, curr.left = self.rec(l, i - 1, index, postorder, indexes)

        return index, curr
