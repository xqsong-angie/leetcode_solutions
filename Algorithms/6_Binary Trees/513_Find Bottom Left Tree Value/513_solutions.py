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
        if not root:#空树没有左下角值
            return 0
        else:
            myqueue.append(root)
            res.append(list(myqueue))
            while len(myqueue)!=0:
                cur=myqueue.pop(0)
                if cur.right:
                    myqueue.append(cur.right)
                if cur.left:
                    myqueue.append(cur.left)
                res.append(list(myqueue))
            res.pop()
        return res[-1][0].val #就是bfs， 然后找到最后一层的元素
    
#20260710 看了一遍（但是上面这个解法很诡异，其实完全可以做普通的层序遍历，然后取最后一层的[0]节点）
