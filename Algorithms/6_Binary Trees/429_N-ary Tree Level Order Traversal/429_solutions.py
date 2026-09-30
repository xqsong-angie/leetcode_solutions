#20260930 AC
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        else:
            res=[]
            path=[]
            length=1
            queue=deque([root])
            while queue:
                while length:
                    cur=queue.popleft()
                    path.append(cur.val)
                    for ch in cur.children:
                        queue.append(ch)
                    length-=1
                res.append(path)
                path=[]
                length=len(queue)
            return res
        