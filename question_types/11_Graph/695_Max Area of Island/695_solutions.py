#dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        cur=0
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        def dfs(grid,visited,x,y):
            direction=[[0,-1],[1,0],[0,1],[-1,0]]
            cur=1
            visited[x][y]=True
            for i in range(4):
                if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:
                    if grid[x+direction[i][1]][y+direction[i][0]]==1 and visited[x+direction[i][1]][y+direction[i][0]]==False:
                        cur+=dfs(grid,visited,x+direction[i][1],y+direction[i][0])
            return cur

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    cur=dfs(grid,visited,i,j)
                    res=max(res,cur)
                    cur=0
        return res
    
#bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        cur=0
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        queue=[]
        def bfs(grid,visited,queue,x,y):
            direction=[[0,-1],[1,0],[0,1],[-1,0]]
            cur=0
            for i in range(4):
                if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:
                    if grid[x+direction[i][1]][y+direction[i][0]]==1 and visited[x+direction[i][1]][y+direction[i][0]]==False:                
                        visited[x+direction[i][1]][y+direction[i][0]]=True
                        cur+=1
                        queue.append((x+direction[i][1],y+direction[i][0]))
            return cur

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    cur=1
                    visited[i][j]=True
                    cur+=bfs(grid,visited,queue,i,j)
                    while queue:
                        cur_pos=queue.pop(0)
                        cur+=bfs(grid,visited,queue,cur_pos[0],cur_pos[1])
                    res=max(res,cur)
                    cur=0
        return res