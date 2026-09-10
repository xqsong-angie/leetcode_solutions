#20260725
#错：
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        offset=1
        start_x=0
        start_y=0
        m=len(matrix)
        n=len(matrix[0])
        loop=max(m,n)//2#🔥应该根据最短边判断 because the short edge runs out of space first
        while offset<=loop:
            #遍历最上方
            for i in range(start_y,n-offset):
                res.append(matrix[start_x][i])
            #遍历最右侧
            for i in range(start_x,m-offset):
                res.append(matrix[i][start_y])
            #遍历最下方
            for i in range(n-offset,start_y,-1):
                res.append(matrix[start_x][i])
            #遍历最左侧
            for i in range(m-offset,start_x,-1):
                res.append(matrix[i][start_y])
            start_x+=1
            start_y+=1
            offset+=1
        return res
        
#对(更推荐四个指针的写法）：
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        #四条边遍历的初始位置
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. 向右遍历上边界
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # 上边界收缩
            
            # 2. 向下遍历右边界
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # 右边界收缩
            
            # 必须判断 top <= bottom，防止单行矩阵收缩后重复遍历
            if top <= bottom:
                # 3. 向左遍历下边界
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # 下边界收缩
            
            # 必须判断 left <= right，防止单列矩阵收缩后重复遍历
            if left <= right:
                # 4. 向上遍历左边界
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # 左边界收缩
                
        return res