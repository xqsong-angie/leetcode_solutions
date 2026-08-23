#20260822
class Solution:
    def solution(self,matrix):
        max_len=0
        cur_len=0
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==1:
                   cur_len+=1
                   
                   #to top left
                   r,c=i,j
                   d=1
                   while 0<=r-d<=row and 0<=c-d<=col:
                    if d%2==0 and matrix[r-d][c-d]==0:#should be 0
                        cur_len+=1
                    elif d%2==1 and matrix[r-d][c-d]==2:#should be 2
                        cur_len+=1
                    else:
                        max_len=max(max_len,cur_len)
                        cur_len=0
                    r=r-d #🔥这里更新完了，上面又r-d，相当于r-2d
                    c=c-d
                
                    #to top right
                    r,c=i,j
                    d=1
                    while 0<=r-d<=row and 0<=c+d<=col:
                        if d%2==0 and matrix[r-d][c+d]==0:#should be 0
                            cur_len+=1#🔥探索新方向，cur_len要重置
                        elif d%2==1 and matrix[r-d][c+d]==2:#should be 2
                            cur_len+=1
                        else:
                            max_len=max(max_len,cur_len)
                            cur_len=0
                        r=r-d
                        c=c+d

                   #to bottom left
                   r,c=i,j
                   d=1
                   while 0<=r+d<=row and 0<=c-d<=col:
                        if d%2==0 and matrix[r+d][c-d]==0:#should be 0
                            cur_len+=1
                        elif d%2==1 and matrix[r+d][c-d]==2:#should be 2
                            cur_len+=1
                        else:
                            max_len=max(max_len,cur_len)
                            cur_len=0
                        r=r+d
                        c=c-d

                   #to bottom right
                   r,c=i,j
                   d=1
                   while 0<=r+d<=row and 0<=c+d<=col:
                        if d%2==0 and matrix[r+d][c+d]==0:#should be 0
                            cur_len+=1
                        elif d%2==1 and matrix[r+d][c+d]==2:#should be 2
                            cur_len+=1
                        else:
                            max_len=max(max_len,cur_len)
                            cur_len=0
                        r=r+d
                        c=c+d
        return max_len
    
#对：
class Solution:
    def solution(self, matrix):
        if not matrix or not matrix[0]:
            return 0
            
        row = len(matrix)
        col = len(matrix[0])
        max_len = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] != 1:
                    continue

                # 4个斜向移动方向: (row方向, col方向)
                directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

                # 如果起点 1 本身就在边界上，最短合法长度至少为 1
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    max_len = max(max_len, 1)

                for dr, dc in directions:
                    r, c = i, j
                    cur_len = 1  # 每次探索新方向，独立重置长度

                    while True:
                        r += dr
                        c += dc

                        # 1. 检查是否超出矩阵边界
                        if not (0 <= r < row and 0 <= c < col):
                            break

                        # 2. 依据当前步数判断期望值 (第1步为2，第2步为0，第3步为2...)
                        expected = 2 if cur_len % 2 == 1 else 0

                        if matrix[r][c] == expected:
                            cur_len += 1
                            # 🔥只有当当前位置处于矩阵边界时，才更新合法最大长度，如果没达到边就断了，就不要
                            if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                                max_len = max(max_len, cur_len)
                        else:
                            # 模式中断
                            break

        return max_len