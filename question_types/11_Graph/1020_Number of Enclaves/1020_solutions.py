class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        def dfs(grid,x,y):
            direction=[[0,-1],[1,0],[0,1],[-1,0]]
            for i in range(4):
                if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:              
                    if grid[x+direction[i][1]][y+direction[i][0]]==1:
                        grid[x+direction[i][1]][y+direction[i][0]]=0
                        dfs(grid,x+direction[i][1],y+direction[i][0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        grid[i][j]=0 #erase all islands that are not enclaves
                        dfs(grid,i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res+=1
        return res