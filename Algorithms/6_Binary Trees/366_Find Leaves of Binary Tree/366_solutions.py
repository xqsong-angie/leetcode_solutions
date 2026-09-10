#20260720
#错：
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        res=[]
        def getLeaves(root):
            if not root:
                return []
            else:
                leaves=[]
                stack=[root]
                while root.left:
                    stack.append(root.left)
                while stack:
                    root=stack[-1]
                    if not root.right:#leaf
                        leaves.append(root.val)
                        stack.pop()
                    else:#still not leaf
                        stack.append(root.right)
                return leaves

#对：基于高度的后序遍历
#一个节点在第几批被当作叶子节点收集，完全取决于它距离最底部的“高度”
class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        res = []
        
        # 定义一个辅助函数，返回当前节点的高度（从下往上数，叶子节点高度为0）
        def getHeight(node):
            if not node:
                return -1  # 空节点高度设为-1，这样叶子节点的高度计算出来就是 max(-1, -1) + 1 = 0
            
            # 递归获取左右子树的高度
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # 当前节点的高度
            curr_height = max(left_height, right_height) + 1
            
            # 如果 res 的长度不够，说明我们遇到了一层新的高度，需要加一个空列表
            if curr_height == len(res):
                res.append([])
                
            # 将当前节点的值放入对应高度的列表中
            res[curr_height].append(node.val)
            
            return curr_height
            
        getHeight(root)
        return res