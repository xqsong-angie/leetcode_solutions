# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        myqueue=[]
        res=[]
        if not root:
            return 0
        else:
            cur=root
            myqueue.append(cur)
            res.append(list(myqueue))
            while len(myqueue)!=0:
                cur=myqueue.pop(0)
                if cur.right:
                    myqueue.append(cur.right)
                if cur.left:
                    myqueue.append(cur.left)
                res.append(list(myqueue))
            res.pop()
        return res[-1][0].val