# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:#两个子树都空，不用加了
            return None
        elif not root1:#只有一个子树，就用那个子树的值
            return root2
        elif not root2:#只有一个子树，就用那个子树的值
            return root1
        else:#有两个子树，需要进行合并
            merged_root=TreeNode()
            merged_root.val=root1.val+root2.val #累加
            merged_root.left=self.mergeTrees(root1.left,root2.left) #左子树和左子树相加
            merged_root.right=self.mergeTrees(root1.right,root2.right)#右子树和右子树相加
        return merged_root
    
#20260710 看了一遍