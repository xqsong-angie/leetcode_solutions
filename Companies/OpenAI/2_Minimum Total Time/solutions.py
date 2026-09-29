class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
#参考答案
class Solution:#🔥要寻找包含起终点和tasks内部节点的最小生成子树
    def solution(self,edges,n,startNode,endNode,tasks):#🔥tasks中的点，不在从start到end到简单路径（不绕弯子的走法）上要算两次，否则算一次
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v) #建立邻接表
            adj[v].append(u)
            
        # 标记所有关键节点（必须被子树包含的节点）
        is_key = [False] * n
        for t in tasks:
            is_key[t] = True
        is_key[startNode] = True
        is_key[endNode] = True
        
        subtree_edges = 0
        
        # DFS 遍历：返回以 u 为根的子树中是否包含关键节点
        def dfs_subtree(u: int, p: int) -> bool:
            nonlocal subtree_edges
            has_key = is_key[u]
            
            for v in adj[u]:
                if v != p:
                    if dfs_subtree(v, u):
                        has_key = True
                        subtree_edges += 1  # 包含了关键节点，这条边必须计入子树
                        
            return has_key

        # DFS 寻找 startNode 到 endNode 的距离
        def dfs_dist(u: int, p: int, depth: int) -> int:
            if u == endNode:
                return depth
            for v in adj[u]:
                if v != p:#直接跳过父节点（不往回走）
                    d = dfs_dist(v, u, depth + 1)
                    if d != -1:#如果在 v 的子树里找到了 endNode
                        return d 
            return -1#🔥在整条分支走到底都没找到 endNode 时才返回-1

        # 1. 计算最小生成子树的边数
        dfs_subtree(startNode, -1)
        
        # 2. 计算 startNode 到 endNode 的最短距离
        dist_start_end = dfs_dist(startNode, -1, 0)
        
        # 3. 套用公式计算结果
        return 2 * subtree_edges - dist_start_end#分支边必须走回头路（往返 2 次），主干边只需要走单程（1 次）