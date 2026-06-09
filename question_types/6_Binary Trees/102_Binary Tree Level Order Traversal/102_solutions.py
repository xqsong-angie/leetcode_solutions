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
            
#20260608
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[List[int]]]:
        if not root:
            return []
            
        queue = [root]
        res = []
        
        while queue:
            # 1. 核心：先记录当前这一层一共有多少个节点
            level_size = len(queue)
            current_level = []  # 用来存当前这一层的节点值
            
            # 2. 严格循环 level_size 次，把当前层的节点全部吐出来
            for _ in range(level_size):
                cur = queue.pop(0)  # 弹出队头
                current_level.append(cur.val)
                
                # 3. 把下一层的节点推入队尾（它们不会影响本次 for 循环，因为 level_size 已经固定了）
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            # 4. 把这一层打包好的结果放入大列表
            res.append(current_level)
            
        return res


            
