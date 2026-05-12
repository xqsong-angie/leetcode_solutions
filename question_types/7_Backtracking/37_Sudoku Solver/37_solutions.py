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
                    ch = board[r][c]
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r//3)*3 + c//3].add(ch)

        def backtracking(r, c):
            if r == n:
                return True
            nr, nc = (r*n+c+1)//n, (r*n+c+1)%n
            if board[r][c] != ".":
                return backtracking(nr, nc)

            box_id = (r//3)*3 + c//3
            for i in range(1, n+1):
                ch = str(i)
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_id]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_id].add(ch)

                    if backtracking(nr, nc):
                        return True

                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_id].remove(ch)

            return False

        backtracking(0, 0)