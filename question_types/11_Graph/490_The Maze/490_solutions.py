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
