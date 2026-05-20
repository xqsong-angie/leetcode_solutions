class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result=[]
        m=len(heights)
        n=len(heights[0])
        if m==1 and n==1:
            return [[0,0]]
        else:
            pacific=[ [False for _ in range(n)] for _ in range(m)]
            atlantic=[ [False for _ in range(n)] for _ in range(m)]
            def dfs(heights,visited,x,y):
                if not visited[x][y]:
                    return
                direction=[[0,-1],[1,0],[0,1],[-1,0]]
                for i in range(4):
                    if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:
                        if not visited[x+direction[i][1]][y+direction[i][0]] and heights[x+direction[i][1]][y+direction[i][0]]>=heights[x][y]:
                            visited[x+direction[i][1]][y+direction[i][0]]=True
                            dfs(heights,visited,x+direction[i][1],y+direction[i][0])

            for i in range(m):
                pacific[i][0]=True
                dfs(heights,pacific,i,0)
                atlantic[i][n-1]=True
                dfs(heights,atlantic,i,n-1)
            
            for j in range(n):
                pacific[0][j]=True
                dfs(heights,pacific,0,j)
                atlantic[m-1][j]=True
                dfs(heights,atlantic,m-1,j)
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j]==True and atlantic[i][j]==True:
                    result.append([i,j])

        return result