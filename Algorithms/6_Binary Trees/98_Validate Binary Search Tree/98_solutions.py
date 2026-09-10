# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.maxVal = None 

        def inorder(node):#左中右
            if not node:#走到底了
                return True

            if not inorder(node.left): #inorder()表示当前节点下是否符合顺序，如果为True不return
                return False

            if self.maxVal is not None and node.val <= self.maxVal:  #self.maxVal是前一个节点的值，如果我比前一个小，说明没按顺序
                return False

            self.maxVal = node.val
            return inorder(node.right)#如果右子树返回True了，就返回True,整棵子树已经看完了

        return inorder(root)
    
#20260710 看了一遍：不能根节点根直接左右孩子比较，比如[10,5,15,null,null,6,20] 感觉有点不熟