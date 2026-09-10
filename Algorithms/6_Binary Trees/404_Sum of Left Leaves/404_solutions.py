# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
                
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:#空树肯定是没有左子树的
            return 0
        else:
            cur=root
            if not cur.left and not cur.right: #这个子树只有根，说明下面也不会有左子树了
                return 0
            else:
                if cur.left and not cur.left.left and not cur.left.right: #left leaf （当前节点有左子树，且左子树没有左子树和右子树，即说明当前节点为左叶子）
                    return cur.left.val+self.sumOfLeftLeaves(cur.right) #求和，左子树看完了，该看右子树
                elif cur.left or cur.right: #not leaf, and the left child is not leaf （当前节点有左或右子树，但是左子树根节点不是叶子）
                    return self.sumOfLeftLeaves(cur.left)+self.sumOfLeftLeaves(cur.right)#那就得分别对左子树右子树递归了

#20260710 看了一遍

#20260726
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.cur_sum=0
        def preorder(root):
            if root.left:
                if not root.left.left and not root.left.right:#left leaf
                    self.cur_sum+=root.left.val
                else:
                    preorder(root.left)
            if root.right:
                preorder(root.right)
        preorder(root)
        return self.cur_sum
