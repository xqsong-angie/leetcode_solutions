#20260704
#错：
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=""
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        m=len(board)
        n=len(board[0])

        def backtracking(x,y,path):#传path是很低效的做法，应该传索引
            path+=board[x][y]
            board[x][y]="0"
            if path==word:#这种比对很低效
                return True
            else:
                for dx,dy in direction:
                    nx=x+dx
                    ny=y+dy
                    if nx>=0 and nx<m and ny>=0 and ny<n and board[nx][ny]!="0":
                        backtracking(nx,ny,path)
                        path=path[:-1]
        #！！！这里默认从棋盘的左上角开始了
        backtracking(0,0,path)
        return False
#对：
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        m=len(board)
        n=len(board[0])

        def backtracking(x,y,idx): #换成传索引
            if idx == len(word) - 1:
                return True
            else:
                temp = board[x][y]#保存当前字符，并标记为已访问，防止重复走，temp是为了回溯的时候再把标记改回来
                board[x][y] = "0"

                for dx,dy in direction:
                    nx=x+dx
                    ny=y+dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx + 1]:
                        #如果深层找到了，立刻一层层往上返回 True
                        if backtracking(nx, ny, idx + 1):
                            return True
                board[x][y] = temp
                return False

        for i in range(m):
            for j in range(n): #！！！用双重循环遍历每一个格子为起点的情况
                if board[i][j] == word[0]: #只有当棋盘字符和单词首字母相同时，才启动回溯，有效剪枝
                    if backtracking(i,j,0):
                        return True #如果首字母不对backtracking(i,j,0)返回False了，注意什么都不要返回!因为接下来还会有其他首字母有可能可以的
        return False