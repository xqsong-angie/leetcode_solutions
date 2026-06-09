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
        
#20260608
#recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,res):
        if root.left:
            res=self.inorder(root.left,res)
        res.append(root.val)
        if root.right:
            res=self.inorder(root.right,res)
        return res
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            self.inorder(root,res)
        return res

#iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        
        # 注意：这里循环条件是 cur 或 stack 不为空
        while cur or stack:
            # 1. 一路向左，把所有的左子节点灌进栈里
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # 2. 走到尽头了，弹出栈顶节点（它是当前最左边的节点）
            cur = stack.pop()
            res.append(cur.val)  # 此时收集结果（左/根）
            
            # 3. 转向右子树
            cur = cur.right
            
        return res