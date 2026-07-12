class Solution:
    def isValid(self,r,c,n):
        #不需要同行，因为回溯保证一行只有一个，不需要查bottom，因为还没排到底下呢
        #same col 
        temp_r=r
        temp_c=c
        for i in range(n):
            if temp_r!=i and self.path[i][temp_c]=='Q':#在当前列，除了这个位置还有没有其他位置有Q
                return False

        #same diagonal(top-left)
        temp_r=r
        temp_c=c
        while temp_r>0 and temp_c>0:#注意别越界
            if self.path[temp_r-1][temp_c-1]=='Q':#在当前对角线，除了这个位置还有没有其他位置有Q
                return False
            else:#横纵坐标一起向左上移动
                temp_r-=1
                temp_c-=1

        #same diagonal(top-right)
        temp_r=r
        temp_c=c
        while temp_r>0 and temp_c<n-1:#注意别越界
            if self.path[temp_r-1][temp_c+1]=='Q':#在当前对角线，除了这个位置还有没有其他位置有Q
                return False
            else:#横纵坐标一起向右上移动
                temp_r-=1
                temp_c+=1

        return True


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res=[] 
        self.path=[["."]*n for _ in range(n)] #每个path都是一张完整的棋盘
        row_pt=0#每层管确定一行的位置（放一个Q在一行）
        def backtracking(row_pt,n):
            if row_pt<n:#还没放到最后一行，继续尝试
                for i in range(n):
                    self.path[row_pt][i]="Q"
                    if self.isValid(row_pt,i,n):
                        backtracking(row_pt+1,n)#只在有效分支上继续试验
                    self.path[row_pt][i]="."#回溯pop
            else:#准备收集结果
                current_board = ["".join(row) for row in self.path]
                self.res.append(current_board)

        backtracking(row_pt,n)
        return self.res
    
#20260711 看了一遍