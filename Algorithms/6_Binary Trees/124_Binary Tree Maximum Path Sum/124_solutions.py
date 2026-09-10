#20260711
#错：
"""
对path的定义理解错了，要一笔画能完成的sequence
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def findMax(cur,max_sum):
            if max_sum<0:
                max_sum=max(max_sum,cur.val)
            elif max_sum>=0 and cur.val>=0:
                max_sum+=cur.val
   
            if cur.left:
                max_sum_left=findMax(cur.left,max_sum)-cur.val
                if max_sum_left>=0:
                    max_sum+=max_sum_left
            if cur.right:
                max_sum_right=findMax(cur.right,max_sum)-cur.val
                if max_sum_right:
                    max_sum+=max_sum_right

            return max_sum

        max_sum=findMax(root,-1001)
        return max_sum
#对：
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 1. 用一个全局变量记录全场最高分
        self.maxSum = -1001

        def getGain(node):
            if not node:
                return 0#不累加，但是要返回数值
            
            # 2. 递归算左边和右边能带来的“最大收益”
            # 如果子树收益是负数，我们直接不要它
            left_gain = max(getGain(node.left), 0)
            right_gain = max(getGain(node.right), 0)
            
            # 3. 【核心冲刺】把当前节点作为“最高拐点”（连通左右）
            # 算出这条完整的拱形路径总和
            current_path_sum = node.val + left_gain + right_gain
            
            # 看看这条路径能不能打破全场世界纪录
            self.maxSum = max(self.maxSum, current_path_sum)
            
            # 4. 【核心返回】向上一层父节点汇报时，不能开叉！
            # 只能在左边和右边挑一条更粗的腿，连着自己一起递给上面
            return node.val + max(left_gain, right_gain)

        getGain(root)
        return self.maxSum