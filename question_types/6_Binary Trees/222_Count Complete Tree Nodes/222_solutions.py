# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height_left(self,cur:Optional[TreeNode]) -> int:
        layer=1
        left=cur.left
        while left:
            left=left.left
            layer+=1
        return layer

    def height_right(self,cur:Optional[TreeNode]) -> int:
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
            if left_height==right_height:
                return 2**left_height-1
            else:
                return 1+self.countNodes(cur.left)+self.countNodes(cur.right)



        