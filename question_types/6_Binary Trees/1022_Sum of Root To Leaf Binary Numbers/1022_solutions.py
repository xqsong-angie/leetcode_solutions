#20260726
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=[]
        def dfs(root,path):
            if not root.left and not root.right:#leaf
                res.append(int(path+str(root.val),2))#https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
            else:
                path+=str(root.val)#🔥字符串是不可变结构，所以每次加字符串都创建了副本，副本之间不相互干扰，不需要pop()做显式回溯，如果是list就需要
                if root.left:
                    dfs(root.left,path)
                if root.right:
                    dfs(root.right,path)
            
        dfs(root,"")
        return sum(res)
    
