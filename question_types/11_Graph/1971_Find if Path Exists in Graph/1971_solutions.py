from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 预构建邻接表：O(E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            cur = queue.popleft()  # O(1)
            if cur == destination:
                return True
            for nei in graph[cur]:  # 只遍历邻居，不是所有边
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        return False