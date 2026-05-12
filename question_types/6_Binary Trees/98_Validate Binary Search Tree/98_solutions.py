# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.maxVal = None 

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.maxVal is not None and node.val <= self.maxVal:
                return False

            self.maxVal = node.val
            return inorder(node.right)

        return inorder(root)