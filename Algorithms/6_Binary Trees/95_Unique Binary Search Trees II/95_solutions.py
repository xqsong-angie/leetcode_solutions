#20261001
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        self.res=[]
        self.root=None
        def backtracking(n,pt):
            if pt<n:
                for i in range(pt,n):
                    node=TreeNode(val=i)
                    if not root:
                        self.root=node
                    backtracking(n,i+1,root.right)
            else:
                self.res.append(self.root.copy())
                self.root #🔥这里不知道如何断开回溯
        backtracking(n,1)

#参考答案
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []
            
        # 定义内部函数：生成由区间 [start, end] 组成的所有可能的 BST
        def build_trees(start: int, end: int) -> list[TreeNode | None]:
            # base case：如果 start > end，说明没有节点，返回 [None] 占位
            if start > end:
                return [None]
            
            all_trees = []
            
            # 尝试把区间内的每一个数字 i 作为当前的根节点
            for i in range(start, end + 1):
                # 递归获取所有可能的左子树集合 (由 start 到 i-1 组成)
                left_trees = build_trees(start, i - 1)
                
                # 递归获取所有可能的右子树集合 (由 i+1 到 end 组成)
                right_trees = build_trees(i + 1, end)
                
                # 笛卡尔积：从左子树集合中挑一棵，右子树集合中挑一棵，拼接到根节点 i 上
                for l in left_trees:
                    for r in right_trees:
                        # 🔥每次这里都新建一个根节点，所以不需要去“断开/复原”以前的节点
                        curr_root = TreeNode(i)
                        curr_root.left = l
                        curr_root.right = r
                        all_trees.append(curr_root)
                        
            return all_trees
            
        return build_trees(1, n)#🔥自底向上，从外向里