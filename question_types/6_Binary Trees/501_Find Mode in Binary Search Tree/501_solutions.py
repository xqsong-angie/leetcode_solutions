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
                else: #如果最后值不一样才更新，最后一个值如果一样就跳出循环了（但是如果这个数此时变成众数，没有同步到result里面）
                    if self.maxCnt==self.count:#处理好几个众数的情况
                        self.result.append(self.prev.val)
                    elif self.maxCnt<self.count:
                        self.maxCnt=self.count
                        self.result=[]#发现更众的数了，之前都清空
                        self.result.append(self.prev.val)#换上新的
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
    
#20260710 看了一遍，以上代码能跑通，但有点问题
