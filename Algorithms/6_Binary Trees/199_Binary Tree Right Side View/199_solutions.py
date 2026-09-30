#20260930 AC
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        else:
            path=[]
            res=[]
            queue=deque([root])
            length=1
            while queue:
                while length:
                    cur=queue.popleft()
                    path.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    length-=1
                res.append(path[-1])
                path=[]
                length=len(queue)
            return res
