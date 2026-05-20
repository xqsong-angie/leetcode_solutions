#bfs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Base case: start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # 8 directions: up, down, left, right, and 4 diagonals
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # Queue stores tuples of (row, col, current_path_length)
        queue = deque([(0, 0, 1)])
        
        # Mark the starting cell as visited by modifying the grid directly
        grid[0][0] = 1
        
        while queue:
            r, c, length = queue.popleft()
            
            # If we reached the bottom-right corner, return the length
            if r == n - 1 and c == n - 1:
                return length
            
            # Explore all 8 adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor is within bounds and is a clear path (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    # Mark as visited IMMEDIATELY to prevent redundant additions to the queue
                    grid[nr][nc] = 1
                    queue.append((nr, nc, length + 1))
                    
        # If the queue empties without reaching the target
        return -1
    
#A*
import heapq
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        #如果起终点不为0走不了
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        def h(r, c):
            return max(n-1-r, n-1-c)  # Chebyshev 距离，(n-1,n-1)是右下角坐标
        
        # 改动1：deque → 最小堆，存 (f, g, r, c)
        heap = [(h(0, 0) + 1, 1, 0, 0)]  # f = g（实际段） + h（估计段），g初始=1
        visited = set() 
        grid[0][0] = 1
        
        while heap:
            f, g, r, c = heapq.heappop(heap)  # 改动2：每次取 f 最小的

            if (r, c) in visited:  # 改动2：出队时检查
                continue
            visited.add((r, c))    # 改动3：出队时才标记

            if r == n-1 and c == n-1:
                return g
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    ng = g + 1
                    nf = ng + h(nr, nc)    # 改动3：算 f = g + h
                    heapq.heappush(heap, (nf, ng, nr, nc))
        
        return -1