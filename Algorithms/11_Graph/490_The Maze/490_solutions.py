#20260720
#错：何时return False?
from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # write your code here
        direction=[[-1,0],[1,0],[0,1],[0,-1]]
        m=len(maze)
        n=len(maze[0])
        visited=[[False]*n for _ in range(m)]
        def dfs(x,y):
            if x==destination[0] and y==destination[1]:#reached dest
                return True
            for dx,dy in direction:
                nx=x+dx
                ny=y+dy
                while 0<=nx<m and 0<=ny<n and maze[nx][ny]!=1 and not visited[nx][ny]:
                    nx+=dx
                    ny+=dy
                nx-=dx
                ny-=dy
                dfs(nx,ny)
        return dfs(start[0],start[1])

#对：
from typing import List

class Solution:
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y):
            # 1. 终点判断
            if x == destination[0] and y == destination[1]:
                return True
            
            # 【核心点 1】：一进入停靠点，立刻标记 visited！只有停下才记录
            visited[x][y] = True
            
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                
                # 【核心点 2】：while 只管撞墙/越界，绝对不检查 visited！可以路过visited, 只要不停靠
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                
                # 退回一步，得到球最终停靠的坐标
                nx -= dx
                ny -= dy
                
                # 【核心点 3】：球停下来后，才检查这个【停靠点】是不是访问过
                if not visited[nx][ny]:
                    if dfs(nx, ny):  # 记得要接收并传递 True！
                        return True
                        
            return False
            
        return dfs(start[0], start[1])
    
#20260724 看了一遍

"""
总结：
bfs: 最小距离路径
dfs: 路径总条数，列出所有可行路径
都可：是否存在路径
"""