# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif key==root.val:
            if not root.left and not root.right:
                return None
            elif not root.left: #and root.right
                return root.right
            elif not root.right: #and root.left
                return root.left
            else: #root.left and root.right
                cur=root.left
                while cur.right:
                    cur=cur.right
                cur.right=root.right
                return root.left
        elif key<root.val:
            if not root.left:
                return root
            else:
                root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            if not root.right:
                return root
            else:
                root.right=self.deleteNode(root.right,key)
        return root
            


