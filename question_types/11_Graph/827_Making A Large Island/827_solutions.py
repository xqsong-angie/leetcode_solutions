class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[0 for _ in range(n)] for _ in range(m)]
        grid_map={0:0}
        count=0
        max_size=0
        mark=1
        direction=[[0,-1],[1,0],[0,1],[-1,0]]

        def dfs(grid, visited, x, y, mark,count):
            visited[x][y]=mark
            count+=1
            for dx,dy in direction:
                if x+dx>=0 and x+dx<=m-1 and y+dy>=0 and y+dy<=n-1 and grid[x+dx][y+dy]==1 and not visited[x+dx][y+dy]:
                    count=dfs(grid, visited, x+dx,y+dy,mark,count)
            return count
        
        for i in range(m):
            for j in range(n):#给每一块连续的陆地标不一样的数字
                if not visited[i][j] and grid[i][j]==1:
                    count=dfs(grid,visited,i,j,mark,count)
                    grid_map[mark]=count#统计每一块陆地大小
                    mark+=1
                    count=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:#海洋
                    grid_set=set()#查看是否该陆地被遍历过
                    cur=1#加一格陆地
                    for dx,dy in direction:#看相邻的位置有没有空位
                        if i+dx>=0 and i+dx<=m-1 and j+dy>=0 and j+dy<=n-1 and grid[i+dx][j+dy]==1:
                            if visited[i+dx][j+dy] not in grid_set:#如果相邻的位置有其他没遍历过的陆地，就加上
                                cur+=grid_map[visited[i+dx][j+dy]]#count大小
                                grid_set.add(visited[i+dx][j+dy])#把该陆地对应的标号记录下来
                    max_size=max(max_size,cur)
                    
        if max_size==0:#说明没有任何海洋，整块是一个陆地
            max_size=m*n

        return max_size
        
#20260723 看了一遍 稍微有点难