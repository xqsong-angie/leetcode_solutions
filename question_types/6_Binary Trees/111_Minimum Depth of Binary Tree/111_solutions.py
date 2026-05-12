# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def counter(self,cur:Optional[TreeNode]):
        if not cur:
            return 0
        elif not cur.left and not cur.right: #leaf node
            return 1
        else: #at least one child(not leaf node)
            left_depth=self.counter(cur.left)
            right_depth=self.counter(cur.right)
            if left_depth==0 or right_depth==0:
                return 1+max(left_depth,right_depth) #one of the tree cannot be zero
            else:
                return 1+min(left_depth,right_depth)


    def minDepth(self, root: Optional[TreeNode]) -> int:

        return self.counter(root)

                

        