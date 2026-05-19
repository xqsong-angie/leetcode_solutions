# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robTree(self, root: Optional[TreeNode]):
        if not root:
            return [0,0]
        else:
            left  = self.robTree(root.left)
            right=self.robTree(root.right)
            #不偷当前节点
            val1=max(left [0],left[1])+max(right[0],right[1])
            #偷当前节点
            val2=root.val+left[0]+right[0]
            return [val1,val2]

    def rob(self, root: Optional[TreeNode]) -> int:
        result=self.robTree(root)
        return max(result)

