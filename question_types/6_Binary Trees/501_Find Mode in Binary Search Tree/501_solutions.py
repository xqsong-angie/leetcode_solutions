# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev=None
        self.result=[]
        self.count=0
        self.maxCnt=0

        def inorder(root:Optional[TreeNode]):
            if not root:
                return
            else:
                inorder(root.left)
                if not self.prev:
                    self.count=1
                elif root.val==self.prev.val:
                    self.count+=1
                else:
                    if self.maxCnt==self.count:
                        self.result.append(self.prev.val)
                    elif self.maxCnt<self.count:
                        self.maxCnt=self.count
                        self.result=[]
                        self.result.append(self.prev.val)
                    self.count=1
                self.prev=root
                inorder(root.right)

        #这两段没写出来
        inorder(root)
        if self.prev:
            if self.count == self.maxCnt:
                self.result.append(self.prev.val)
            elif self.count > self.maxCnt:
                self.result = [self.prev.val]

        return self.result
    
                