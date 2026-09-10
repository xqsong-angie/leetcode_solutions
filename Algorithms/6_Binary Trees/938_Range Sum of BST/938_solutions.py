#20260727
#错：
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        else:
            left=right=0
            if low<=root.val<=high:
                if root.left:
                    left=self.rangeSumBST(root.left, low, high)
                if root.right:
                    right=self.rangeSumBST(root.right, low, high)
                return root.val+left+right#unsupported operand type(s) for +: 'int' and 'NoneType'
            elif root.val<low:
                if root.right:
                    right=self.rangeSumBST(root.right, low, high)
                return left+right
            elif root.val>high and root.left:#🔥root.val>high 但没有左子树的情况没法处理了
                if root.left:
                    left=self.rangeSumBST(root.left, low, high)
                return left+right
#对：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        else:
            left=right=0
            if low<=root.val<=high:
                if root.left:
                    left=self.rangeSumBST(root.left, low, high)
                if root.right:
                    right=self.rangeSumBST(root.right, low, high)
                return root.val+left+right
            elif root.val<low:
                if root.right:
                    right=self.rangeSumBST(root.right, low, high)
                return left+right
            elif root.val>high:
                if root.left:
                    left=self.rangeSumBST(root.left, low, high)
                return left+right