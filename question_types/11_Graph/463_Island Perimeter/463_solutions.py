class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #本题不用搜
        m=len(grid)
        n=len(grid[0])
        count=0
        direction=[[0,-1],[1,0],[0,1],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    for dx,dy in direction:
                        if i+dx<0 or i+dx>m-1 or j+dy<0 or j+dy>n-1 or grid[i+dx][j+dy]==0:
                            count+=1
        return count


