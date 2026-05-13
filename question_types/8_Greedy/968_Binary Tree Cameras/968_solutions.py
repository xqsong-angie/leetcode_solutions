# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #0:无覆盖, 1: 放摄像头 2:没摄像头但是有覆盖
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt=0
        def traversal(node): #返回的是状态（数值）
            if not node:
                return 2
            else:
                left_val=traversal(node.left)
                right_val=traversal(node.right)
                if left_val==2 and right_val==2: 
                    return 0
                elif left_val==0 or right_val==0:
                    self.cnt+=1
                    return 1    
                elif left_val==1 or right_val==1:
                    return 2

        if traversal(root)==0:
            return self.cnt+1
        else:
            return self.cnt



            
