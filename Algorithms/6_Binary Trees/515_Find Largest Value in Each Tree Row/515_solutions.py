#20260720
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            res=[]
            queue=[root]
            while queue:
                length=len(queue)
                layer=[]
                while length:
                    cur=queue.pop(0)
                    layer.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    length-=1
                res.append(max(layer))
            return res