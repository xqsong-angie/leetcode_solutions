#1.recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        else:
            if root.left:
                res+=self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res+=self.inorderTraversal(root.right)
            return res
        
#2.iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        mystack=[]
        if not root:
            return res
        else:
            cur=root
            while cur or mystack:
                while cur:
                    mystack.append(cur)
                    cur=cur.left
                cur=mystack.pop()
                res.append(cur.val)
                cur=cur.right

            return res