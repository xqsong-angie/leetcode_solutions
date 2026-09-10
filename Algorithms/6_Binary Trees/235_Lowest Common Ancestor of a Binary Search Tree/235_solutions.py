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
        elif root.val==p.val or root.val==q.val: #前面这里都和BT一样
            return root
        else:
            if p.val<root.val and q.val<root.val:#有root比那两个大，说明这两个都在左子树里，最低祖先也一定在左子树里
                return self.lowestCommonAncestor(root.left,p,q)
            elif (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val): #根夹在两个节点之间了，分q<p和p<q两种情况
                return root#那就返回此根
            else:#有root比那两个小，说明这两个都在右子树里，最低祖先也一定在右子树里
                return self.lowestCommonAncestor(root.right,p,q)

#20260710 看了一遍