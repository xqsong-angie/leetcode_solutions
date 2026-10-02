#20261001 AC
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res=[]
        def post(root):
            if not root:
                return 
            else:
                if root.children:  
                    for ch in root.children:
                        post(ch)
                self.res.append(root.val)

        if not root:
            return []
        elif not root.children:
            return [root.val]
        else:
            post(root)
            return self.res
    