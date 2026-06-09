#20251002
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
        
#20260608

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,res):
        if root:
            res.append(root.val)
            self.preorder(root.left,res)
            self.preorder(root.right,res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        res=[]
        res=self.preorder(root,res)
        return res
        
#iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            # 1. 弹出当前要访问的节点
            cur = stack.pop()
            res.append(cur.val)
            
            # 2. 先把右子树压入栈（因为是栈，后进先出，所以右子树后处理）
            if cur.right:
                stack.append(cur.right)
                
            # 3. 再把左子树压入栈（先处理）
            if cur.left:
                stack.append(cur.left)
                
        return res
