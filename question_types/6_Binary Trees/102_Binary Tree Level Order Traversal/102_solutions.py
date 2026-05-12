# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myqueue=[]
        res=[]
        layer=[]
        size=0
        if not root:
            return res
        else:
            cur=root
            myqueue.append(cur)
            size=len(myqueue)
            while myqueue:
                while size>0:
                    cur=myqueue.pop(0)
                    size-=1
                    layer.append(cur.val)  
                    if cur.left:
                        myqueue.append(cur.left)
                    if cur.right:
                        myqueue.append(cur.right)
                size=len(myqueue)
                res.append(layer)
                layer=[]
        return res
            
            
