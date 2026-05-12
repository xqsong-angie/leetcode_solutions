# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root.val==p.val or root.val==q.val:
            return root
        else:
            if p.val<root.val and q.val<root.val:
                return self.lowestCommonAncestor(root.left,p,q)
            elif (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
                return root
            else:
                return self.lowestCommonAncestor(root.right,p,q)
