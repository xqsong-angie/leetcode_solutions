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
        
#20260608
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. 先把左子树和右子树各自翻转好（递归）
        left_side = self.invertTree(root.left)
        right_side = self.invertTree(root.right)
        
        # 2. 根节点最后把它们交换（后序：左右根）
        root.left = right_side
        root.right = left_side
        
        return root #叶子节点情况：因为叶子节点没有左右节点，所以所有上面都执行完，left_side=right_side=None, 来到这一步，函数返回root, 叶子待在原地不动，即invertTree(leaf)==leaf
    
#20260709看了一遍