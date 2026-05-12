#1.recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        else:
            if root.left:
                res+=self.postorderTraversal(root.left)
            if root.right:
                res+=self.postorderTraversal(root.right)
            res.append(root.val)
            return res
        
#2.iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    cur=cur.right
                cur=mystack.pop()
                cur=cur.left
            res.reverse()
            return res