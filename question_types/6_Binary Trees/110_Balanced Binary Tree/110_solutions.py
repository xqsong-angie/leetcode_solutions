# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self,cur: Optional[TreeNode])->int:
        if not cur:
            return 0
        elif not cur.left and not cur.right:
            return 1
        else:
            return 1+max(self.getHeight(cur.left),self.getHeight(cur.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            cur=root
            if abs(self.getHeight(cur.left)-self.getHeight(cur.right))<=1:
                return self.isBalanced(cur.left) and self.isBalanced(cur.right)
            else:
                return False