#20260930 AC
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.max=0

    def helper(self,root,depth):
        if not root.children:
            self.max=max(self.max,depth)
        else:
            for ch in root.children:
                self.helper(ch,depth+1)

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root:
            depth=1
            self.helper(root,depth)
            return self.max

