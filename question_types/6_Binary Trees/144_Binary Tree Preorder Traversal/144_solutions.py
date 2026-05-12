
#1. recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        else:
            res.append(root.val)
            if root.left:
                res+=self.preorderTraversal(root.left)
            if root.right:
                res+=self.preorderTraversal(root.right)
            return res
        
#2. iterative solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        mystack=[]
        if not root:
            return res
        else:
            cur=root
            while cur or mystack:
                while cur:
                    res.append(cur.val)
                    mystack.append(cur)
                    cur=cur.left
                cur=mystack.pop()
                cur=cur.right
            return res