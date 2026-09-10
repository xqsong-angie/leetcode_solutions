# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height_left(self,cur:Optional[TreeNode]) -> int:#这才是真正用来计算高度的函数
        layer=1
        left=cur.left
        while left:
            left=left.left
            layer+=1
        return layer

    def height_right(self,cur:Optional[TreeNode]) -> int:#只是用来看是不是满的
        layer=1
        right=cur.right
        while right:
            right=right.right
            layer+=1
        return layer

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            cur=root
            left_height=self.height_left(cur)
            right_height=self.height_right(cur)
            if left_height==right_height:#可以确定是满二叉树
                return 2**left_height-1#满二叉树节点个数公式
            else:
                return 1+self.countNodes(cur.left)+self.countNodes(cur.right)#不满就无限细分直到能用公式为止



        