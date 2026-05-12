# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, root:Optional[TreeNode] )-> None:
        temp=root.left
        root.left=root.right
        root.right=temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        size=0
        if not root:
            return root
        else:
            cur=root
            self.swap(cur)
            self.invertTree(cur.left)
            self.invertTree(cur.right)
            return root