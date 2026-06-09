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
        
#20260608
#recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,res):
        if root.left:
            res=self.postorder(root.left,res)
        if root.right:
            res=self.postorder(root.right,res)
        res.append(root.val)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            self.postorder(root,res)
        return res
    
#iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        stack = [root]
        res = []
        
        while stack:
            cur = stack.pop()
            # 1. 收集根节点的值
            res.append(cur.val)
            
            # 2. 先压入左子节点（后出栈，先处理右子节点）
            if cur.left:
                stack.append(cur.left)
            # 3. 再压入右子节点（先出栈，后处理左子节点）
            if cur.right:
                stack.append(cur.right)
                
        # 此时 res 的顺序是 根->右->左，翻转后变成 左->右->根
        return res[::-1]