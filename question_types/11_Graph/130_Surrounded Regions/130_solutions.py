class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def dfs(grid,x,y):
            direction=[[0,-1],[1,0],[0,1],[-1,0]]
            for i in range(4):
                if x+direction[i][1]>=0 and x+direction[i][1]<=m-1 and y+direction[i][0]>=0 and y+direction[i][0]<=n-1:
                    if board[x+direction[i][1]][y+direction[i][0]]=="O":
                        board[x+direction[i][1]][y+direction[i][0]]="1"
                        dfs(board,x+direction[i][1],y+direction[i][0])

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i==0 or j==0 or i==m-1 or j==n-1):
                    board[i][j]="1"
                    dfs(board,i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"

        for i in range(m):
            for j in range(n):
                if board[i][j]=="1":
                    board[i][j]="O"