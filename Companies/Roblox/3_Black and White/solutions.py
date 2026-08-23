#20260822
class Solution:
    def back_and_white(self,rows,cols,black):
        res=[0]*5
        grid=[[0]*cols for _ in range(rows)]

        for b in black:
            grid[b[0]][b[1]]=1

        for i in range(rows-1):
            for j in range(cols-1):
                sum=grid[i][j]+grid[i+1][j]+grid[i][j+1]+grid[i+1][j+1]
                res[sum]+=1
        return res
    
#性能优化（哈希表）
from collections import Counter
class Solution:

    def back_and_white(self, rows, cols, black):
        submatrix_counts = Counter()

        # 1. 只遍历黑色格子，计算它影响到的 2x2 子矩阵的左上角 (r, c)
        for r, c in black:
            # 一个黑色格子 (r, c) 最多能作为 4 个 2x2 子矩阵的某一个角
            for dr in (0, -1):
                for dc in (0, -1):
                    top_r, top_c = r + dr, c + dc
                    # 检查该 2x2 子矩阵的左上角坐标是否合法🔥如果左上角合法，那么四个都合法
                    if 0 <= top_r < rows - 1 and 0 <= top_c < cols - 1:
                        submatrix_counts[(top_r, top_c)] += 1

        # 2. 初始化结果数组，索引 0~4 分别对应含有 0~4 个黑格的子矩阵数量
        res = [0] * 5

        # 3. 统计含有 1, 2, 3, 4 个黑格的子矩阵数量
        non_zero_submatrices = 0
        for count in submatrix_counts.values():
            res[count] += 1
            non_zero_submatrices += 1

        # 4. 含有 0 个黑格的子矩阵数量 = 网格中所有 2x2 子矩阵总数 - 含有黑格的子矩阵总数
        total_submatrices = (rows - 1) * (cols - 1)
        res[0] = total_submatrices - non_zero_submatrices

        return res
