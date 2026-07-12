class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)] #空间换时间，从loop比较值到直接set查找O(1)

        # 预处理已有数字
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    ch = board[r][c]#数字
                    rows[r].add(ch)#塞入集合，此行已有该数
                    cols[c].add(ch)#塞入集合，此列已有该数
                    boxes[(r//3)*3 + c//3].add(ch)#宫格内塞入集合

        def backtracking(r, c):
            if r == n:#每层代表一行
                return True
            nr, nc = (r*n+c+1)//n, (r*n+c+1)%n#先算格子总数，倍数和余数分别为行和列
            if board[r][c] != ".":#这里已经放过数字了
                return backtracking(nr, nc)#继续去下一个位置处理

            box_id = (r//3)*3 + c//3#宫格位置
            #当前位置还没有放过数字
            for i in range(1, n+1):
                ch = str(i)
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_id]:#没用过就可以填
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_id].add(ch)#放完数字了

                    if backtracking(nr, nc): #如果backtracking返回的是False, 不返回，说明当前试的这个ch不行，可以换一个说不定就走得通了呢
                        return True

                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_id].remove(ch)

            return False

        backtracking(0, 0)

#20260711 看了一遍