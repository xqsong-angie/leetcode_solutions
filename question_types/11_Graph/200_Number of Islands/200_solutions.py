#dfs
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, visited, x,y,m,n):
            direction=[[0,1],[1,0],[-1,0],[0,-1]]
            if x>=0 and x<=m-1 and y>=0 and y<=n-1:
                if grid[x][y]=="1" and visited[x][y]==False:
                    visited[x][y]=True
                    for i in range(4):          
                        dfs(grid,visited,x+direction[i][0],y+direction[i][1],m,n)

        m=len(grid)
        n=len(grid[0])

        res=0
        visited=[[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    dfs(grid,visited,i,j,m,n)
                    res+=1
        return res
    
#bfs
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:

        m=len(grid)
        n=len(grid[0])
        def bfs(grid,visited,queue,x,y):
            direction=[[0,-1],[1,0],[0,1],[-1,0]]
            for i in range(4):
                if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:
                    if grid[x+direction[i][1]][y+direction[i][0]]=="1" and visited[x+direction[i][1]][y+direction[i][0]]==False:
                        queue.append((x+direction[i][1],y+direction[i][0]))
                        visited[x+direction[i][1]][y+direction[i][0]]=True

        res=0
        visited=[[False for _ in range(n)] for _ in range(m)]
        queue=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j]==False:
                    visited[i][j]=True
                    bfs(grid,visited,queue,i,j) 
                    while queue:
                        cur_pos=queue.pop(0)
                        bfs(grid,visited,queue,cur_pos[0],cur_pos[1])
                    res+=1
        return res