# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        else:
            root=TreeNode()
            root.val=postorder[-1]
            index=0
            for i in range(len(inorder)):
                if root.val==inorder[i]:
                    index=i
                    break
            #recursion for left
            root.left=self.buildTree(inorder[:index],postorder[:index])
            #recursion for right
            root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
            return root