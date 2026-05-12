class Solution:
    def isValid(self,r,c,n):
        #不需要同行，因为回溯保证一行只有一个，不需要查bottom，因为还没排到底下呢
        #same col
        temp_r=r
        temp_c=c
        for i in range(n):
            if temp_r!=i and self.path[i][temp_c]=='Q':
                return False

        #same diagonal(top-left)
        temp_r=r
        temp_c=c
        while temp_r>0 and temp_c>0:
            if self.path[temp_r-1][temp_c-1]=='Q':
                return False
            else:
                temp_r-=1
                temp_c-=1

        #same diagonal(top-right)
        temp_r=r
        temp_c=c
        while temp_r>0 and temp_c<n-1:
            if self.path[temp_r-1][temp_c+1]=='Q':
                return False
            else:
                temp_r-=1
                temp_c+=1

        return True


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res=[] 
        self.path=[["."]*n for _ in range(n)] #每个path都是一张完整的棋盘
        row_pt=0
        def backtracking(row_pt,n):
            if row_pt<n:
                for i in range(n):
                    self.path[row_pt][i]="Q"
                    if self.isValid(row_pt,i,n):
                        backtracking(row_pt+1,n)
                    self.path[row_pt][i]="."
            else:
                current_board = ["".join(row) for row in self.path]
                self.res.append(current_board)

        backtracking(row_pt,n)
        return self.res