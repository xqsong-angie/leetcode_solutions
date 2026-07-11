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
                self.diff = min(self.diff, abs(node.val - self.prev.val)) #跟中序上一个减，更新更小值

            self.prev = node

            inorder(node.right)

        inorder(root)
        return self.diff
    
#20260710 看了一遍