# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
                
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            cur=root
            if not cur.left and not cur.right:
                return 0
            else:
                if cur.left and not cur.left.left and not cur.left.right: #left leaf
                    return cur.left.val+self.sumOfLeftLeaves(cur.right)
                elif cur.left or cur.right: #not leaf, and the left child is not leaf
                    return self.sumOfLeftLeaves(cur.left)+self.sumOfLeftLeaves(cur.right)
