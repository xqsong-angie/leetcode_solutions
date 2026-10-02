#20261001
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init___(self): #🔥这里是三个下划线不是两个
        self.res=[]
        
    def helper(self,root,targetSum,path):
        if not root.left and not root.right:#leaf
            if root.val==targetSum:
                path.append(root.val)
                self.res.append(path) #🔥AttributeError: 'Solution' object has no attribute 'res'
        else:#not leaf 🔥path会按引用传递，且没有回溯
            path.append(root.val)
            self.helper(root.left,targetSum-root.val,path)+self.helper(root.right,targetSum-root.val,path)#🔥分两行调用，helper没有return,不能执行+

    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        elif not root.left and not root.righ:#🔥right拼写少一个t
            if root.val==targetSum:
                return [root.val]
            else:
                return[]
        else:
            self.helper(root.left,targetSum-root.val,[root.val])
            self.helper(root.right,targetSum-root.val,[root.val])
            return self.res
        
#参考答案
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        
        # 定义内部 DFS 函数
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # 1. 做出选择：将当前节点加入路径
            path.append(node.val)
            current_sum -= node.val
            
            # 2. 检查是否满足条件（是叶子节点且路径和正好归零）
            if not node.left and not node.right and current_sum == 0:
                #🔥 注意：必须传入 list(path) 来创建当前路径的副本！
                # 否则后续的 pop() 会把存入 res 的结果也清空
                res.append(list(path)) 
            else:
                # 3. 继续向下递归搜索
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
                
            # 4. 🔥撤销选择（回溯）：在返回上一层前，把当前节点从路径中移除
            path.pop()

        # 从根节点开始搜索
        dfs(root, targetSum, [])
        
        return res