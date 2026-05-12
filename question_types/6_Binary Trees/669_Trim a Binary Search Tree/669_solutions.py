# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            if root.val>=low and root.val<=high:
                root.left=self.trimBST(root.left,low,high)
                root.right=self.trimBST(root.right,low,high)
            elif root.val<low:
                root.left=None
                root=self.trimBST(root.right,low,high)
            else:
                root.right=None
                root=self.trimBST(root.left,low,high)
            return root
