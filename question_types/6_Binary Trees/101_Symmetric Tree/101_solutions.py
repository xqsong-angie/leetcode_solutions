# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self,left:Optional[TreeNode], right:Optional[TreeNode])->bool:
        if not left and right:
            return False
        elif left and not right:
            return False
        elif not left and not right:
            return True
        elif left.val !=right.val:
            return False
        else:#left.val==right.val
            return self.compare(left.left,right.right) and self.compare(left.right,right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)