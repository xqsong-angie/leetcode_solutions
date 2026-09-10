# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:#没得可切了
            return None
        else:
            if root.val>=low and root.val<=high:#根在范围内，看子树
                root.left=self.trimBST(root.left,low,high)
                root.right=self.trimBST(root.right,low,high)
            elif root.val<low:#根就不在范围内，那根及左子树都不能要
                root.left=None#切 
                root=self.trimBST(root.right,low,high)#右子树当新根返回
            else:#根就不在范围内，那根及右子树都不能要
                root.right=None#切
                root=self.trimBST(root.left,low,high)#左子树当新根返回
            return root
#20260711 看了一遍

#20260727
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
            left=right=None
            if low<=root.val<=high:
                left=self.trimBST(root.left, low, high)
                right=self.trimBST(root.right, low, high)
                root.left=left
                root.right=right
                return root
            elif root.val<low:
                return self.trimBST(root.right, low, high)
            elif root.val>high:
                return self.trimBST(root.left, low, high)