#20260711
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://www.geeksforgeeks.org/python/deque-in-python/
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        res=[]#最终结果
        count=1#层数
        length=1#当前层长度
        layer=[]#当前层
        stack=[]#栈
        if not root:
            return []
        while queue:
            while length:
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                length-=1
                layer.append(cur.val)
                
            if count%2==0:
                while layer:
                    stack.append(layer.pop())
                res.append(stack)
                stack=[]
            else:
                res.append(layer)
                layer=[]
            length=len(queue)
            count+=1
        return res

