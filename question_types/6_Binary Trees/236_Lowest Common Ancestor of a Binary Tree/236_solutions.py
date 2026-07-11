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
        elif root.val==p.val or root.val==q.val:#root是其中一个
            return root#那么祖先就是p
        else:#root是p或q
            left=self.lowestCommonAncestor(root.left,p,q)#去左子树找
            right=self.lowestCommonAncestor(root.right,p,q)#去右子树找
            if left and right:#左右子树都找到（找到情况无非两种，一种是在某个子树，根节点就是p或q,那么直接返回根节点即可；也有一种情况，就是p和q在左右子树上，所以返回上来两个）
                return root#返回上来两个的话，那门直系父亲就是那个祖先（lowest)
            elif not left:#说明都在右边
                return right
            else:#说明都在左边
                return left

#20260710 看了一遍