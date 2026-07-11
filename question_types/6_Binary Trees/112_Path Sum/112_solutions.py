# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:#都轮到空子树没有值了，还没有找到，就只能返回False了
            return False
        elif not root.left and not root.right:#子树只有根节点
            return targetSum==root.val#那就看看现在这个根节点的值，能不能满足target， 满足就True, 不满足就False
        else:#子树有左子树或右子树
            return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)#分别对左子树右子树查询，有一个对的就返回True


#20260710 看了一遍
