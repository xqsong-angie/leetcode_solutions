#20260930
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.mymap=defaultdict(int)

    def helper(self,root,target,flag):
        if root.val==target:
            flag=True #found
        else:
            if flag==False:
                self.mymap[root.val]+=1
                self.helper(root.left)
                self.helper(root.right)
                for k,v in self.mymap.items():
                    v+=1
            else:
                #这里的逻辑不是特别好确定🔥太复杂
                pass

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        else:
            res=[]
            self.helper(root,target,False)
            for key,v in self.mymap.items():
                if v==k:
                    res.append(v)
            return res

#答案：转为无向图 + BFS

from collections import deque, defaultdict
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []
        
        # 1. 第一步：DFS 构建 parent 哈希表，记录每个节点的父节点（🔥每个节点的父节点唯一）
        parent = {}
        def build_parent(node, p=None):
            if node:
                parent[node] = p
                build_parent(node.left, node)
                build_parent(node.right, node)
        
        build_parent(root)
        
        # 2. 第二步：从 target 开始做 BFS 扩散
        queue = deque([target])
        visited = {target}  # 防止在父子节点间循环重复访问
        current_distance = 0
        
        while queue:
            # 如果当前扩散步数达到 k，队列里的所有节点就是目标答案
            if current_distance == k:
                return [node.val for node in queue]
            
            # 层序遍历当前层的所有节点
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                # 尝试向三个方向移动：左子节点、右子节点、父节点
                for neighbor in (curr.left, curr.right, parent.get(curr)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            current_distance += 1
            
        return []