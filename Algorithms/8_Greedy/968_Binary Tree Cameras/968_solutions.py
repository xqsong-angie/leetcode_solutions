# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #0:无覆盖, 1: 放摄像头 2:没摄像头但是有覆盖
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt=0#放摄像头个数
        def traversal(node): #返回的是状态（数值）
            if not node:
                return 2
            else:
                left_val=traversal(node.left)#左子树根节点的状态
                right_val=traversal(node.right)#右子树根节点的状态
                if left_val==2 and right_val==2: #这里没有监视到
                    return 0
                elif left_val==0 or right_val==0:#有空位了，这里必须放一个
                    self.cnt+=1
                    return 1    
                elif left_val==1 or right_val==1:#左右有摄像头，这里肯定不用放切已经被监视
                    return 2

        if traversal(root)==0:#补上一个
            return self.cnt+1
        else:
            return self.cnt

#20260712 看了一遍

            
