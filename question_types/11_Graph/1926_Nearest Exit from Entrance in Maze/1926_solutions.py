#20260628
#错：-1 is not valid value for the expected return type integer
import numpy as np
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m=len(maze)
        n=len(maze[0])
        count=[[0]*n for _ in range(m)]
        count[entrance[0]][entrance[1]]=1
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        def bfs(maze,m,n,r,c,count,direction):
            queue=[]
            for i in range(4):
                dr=direction[i][0]
                dc=direction[i][1]
                if r+dr<m and c+dc<n: #🔥越界检查不完整，没有检查下限
                    if maze[r+dr][c+dc]!="+" and count[r+dr][c+dc]==0:
                        queue.append([r+dr,c+dc])
            while queue:
                nxt=queue.pop(0)
                count[nxt[0]][nxt[1]]=count[r][c]+1
                bfs(maze,m,n,nxt[0],nxt[1],count,direction) #🔥标准的bfs不需要递归
            return count
        count=bfs(maze,m,n,entrance[0],entrance[1],count,direction)
        res=np.array(count).min() #https://stackoverflow.com/questions/42536251/python-minimum-value-of-matrix

        return -1 if res==1 else res-1
                    
#对：bfs不需要递归
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m=len(maze)
        n=len(maze[0])
        start_r,start_c=entrance
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        maze[start_r][start_c] = "+" # 🔥在遍历时直接将入口标记为墙，不需要多一个count/visited矩阵
        queue=deque([(start_r, start_c, 0)]) #🔥双端数组比普通数组性能更优，尤其是需要频繁取出头部元素时
        while queue:
            r, c, steps=queue.popleft()

            #🔥先判断当前节点是否在出口，是出口直接return, 因为是bfs一定是最短路径
            if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and (r != start_r or c != start_c):#防止起点是边界的情况
                return steps 

            #再看相邻的四个格子
            for dr,dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[r+dr][c+dc]!="+":
                    maze[nr][nc] = "+" #🔥标墙，替代visited逻辑
                    queue.append((nr, nc, steps + 1))

        return -1 # 队列都空了还是没找到出口，说明出不去
                    
