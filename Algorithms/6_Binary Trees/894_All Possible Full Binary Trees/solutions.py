#20260928
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n==1:
            return [TreeNode(0)]
        else:
            pass
            #🔥想到这里就不知道怎么办了，这题是回溯吗，可是当收集的结果每个元素都是树该怎么回溯啊


#参考答案：不需要回溯，用分治法+动态规划
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.memo = {}

    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        # 1. 偶数节点不可能组成满二叉树 🔥一棵满二叉树（Full Binary Tree）是由 “1个根节点 + 左子树 + 右子树” 组成的
        if n % 2 == 0:
            return []
        
        # 2. 递归基：只有1个节点时，只有一种树结构
        if n == 1:
            return [TreeNode(0)]
        
        # 3. 检查记忆化缓存，避免重复计算左右子树里面节点数相同的情况
        if n in self.memo:
            return self.memo[n]
        
        res = []
        
        # 4. 枚举左子树的节点数 i（从 1 到 n-2，且步长为 2，保证是奇数）
        for i in range(1, n, 2): #🔥n个节点分给一整棵树，根节点消耗一个，桶里左子树也是满二叉树，所以节点数i只能为奇数
            left_nodes = i#🔥设左子树消耗i个
            right_nodes = n - 1 - i#🔥右子树消耗n-1-i个
            
            # 递归获取所有可能的左子树和右子树列表
            left_trees = self.allPossibleFBT(left_nodes)
            right_trees = self.allPossibleFBT(right_nodes)
            
            # 5. 组合：遍历左子树和右子树的所有可能组合
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        
        # 保存答案并返回
        self.memo[n] = res
        return res