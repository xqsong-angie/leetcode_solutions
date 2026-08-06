#20260805
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row validation
        for i in range(9):
            row=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in row :
                    return False
                else:
                    row.add(board[i][j])

        #col validation
        for i in range(9):
            col=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[j][i] in col :
                    return False
                else:
                    row.add(board[j][i])
        
        #box validation🔥本题难点就是box的坐标转换
        for i in range(9):
            col=set()
            for j in range(9):
                if board[i][i+j//3]==".": 
                    continue
                elif board[j][i] in col :
                    return False
                else:
                    row.add(board[j][i])

        return True
    
#对：
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. 验证所有行 (Row validation)
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        # 2. 验证所有列 (Col validation)
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                # 注意遍历列时，行在变(j)，列固定(i)
                if board[j][i] in col:
                    return False
                col.add(board[j][i]) # 修复了这里的 row.add
        
        # 3. 验证所有 3x3 九宫格 (Box validation)
        for i in range(9):
            box = set()
            for j in range(9):
                # 利用公式计算出 9x9 棋盘上的实际坐标
                r = (i // 3) * 3 + j // 3
                c = (i % 3) * 3 + j % 3
                
                if board[r][c] == ".":
                    continue
                if board[r][c] in box:
                    return False
                box.add(board[r][c]) # 修复了这里的 row.add

        return True