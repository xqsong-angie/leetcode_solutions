# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.diff = float("inf")

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.diff = min(self.diff, abs(node.val - self.prev.val))

            self.prev = node

            inorder(node.right)

        inorder(root)
        return self.diff