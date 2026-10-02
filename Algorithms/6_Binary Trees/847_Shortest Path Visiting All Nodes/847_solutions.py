#20261001
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        vis=[[0]*n for _ in range(n)] #从i 点开始的
        while 0 in vis:
            for i in range(n):
                vis[i][i]=1
                for j in range(len(graph[i])):
                    graph[i][j]
                    #🔥如何去计数呢

#答案
from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        # 如果只有一个节点，不需要走，步数为 0
        if n == 1:
            return 0
            
        # 目标状态：n 个位全为 1。例如 n=3，1<<3 是 1000(8)，减 1 变成 0111(7)
        target = (1 << n) - 1 
        
        # 队列中存储元组：(当前节点, 当前访问状态 mask, 当前步数)
        # 题目说可以从任意节点出发，所以我们把所有节点作为起点一起放入队列
        q = deque([(i, 1 << i, 0) for i in range(n)])
        
        # vis 集合用来去重，防止死循环。
        # 这里的“访问过”必须是 (当前节点, 当前状态) 的组合！
        vis = set([(i, 1 << i) for i in range(n)])
        
        while q:
            # 弹出当前状态，step 就是你要的“计数”
            node, mask, step = q.popleft()
            
            # 遍历当前节点的所有邻居
            for neighbor in graph[node]:
                # 使用 按位或 (|) 更新下一个状态。🔥按位或代表只要一个节点至少被访问过一次就算
                # 比如当前 mask 是 001(节点0)，neighbor 是 1(1<<1 = 010)，按位或结果就是 011
                next_mask = mask | (1 << neighbor)
                
                # 如果下一步就达到了目标状态，直接返回 步数 + 1
                if next_mask == target:
                    return step + 1
                
                # 如果这个 (邻居节点, 新状态) 的组合以前没见过，就加入队列
                if (neighbor, next_mask) not in vis:
                    vis.add((neighbor, next_mask))
                    q.append((neighbor, next_mask, step + 1))
                    
        return 0