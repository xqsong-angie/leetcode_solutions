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
        left_depth=self.counter(cur.left)
        right_depth=self.counter(cur.right)
        return 1+max(left_depth,right_depth)


    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.counter(root)

                
