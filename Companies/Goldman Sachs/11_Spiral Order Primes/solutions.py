
class Solution:
    def spiralOrderPrimes(self,grid):
        def isPrime(num):
            if num>=2:
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        return False
                return True
            else:
                return False
            
        rows=len(grid)
        cols=len(grid[0])
        loop=min(rows,cols)//2
        offset=1
        start_x=0
        start_y=0
        res=[]
        count=1
        while count<=loop:
            #top
            for i in range(start_y,cols-offset):
                if isPrime(grid[start_x][i]):
                    res.append(grid[start_x][i])

            #right
            for i in range(start_x,rows-offset):
                if isPrime(grid[i][start_y]):
                    res.append(grid[i][start_y])#🔥边界有问题

            #bottom
            for i in range(cols-offset,start_y,-1):
                if isPrime(grid[start_x][i]):
                    res.append(grid[start_x][i])

            #left
            for i in range(rows-offset,start_x,-1):
                if isPrime(grid[i][start_y]):
                    res.append(grid[i][start_y])

            start_x+=1
            start_y+=1
            offset+=1
            count+=1
        return res

#对：
class Solution:
    def spiralOrderPrimes(self, grid: list[list[int]]) -> list[int]:
        if not grid or not grid[0]:
            return []

        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        rows, cols = len(grid), len(grid[0])
        top, bottom = 0, rows - 1 #🔥提前标号在哪行/哪列遍历，不容易弄错
        left, right = 0, cols - 1
        res = []

        while top <= bottom and left <= right:
            # 1. 从左到右遍历顶行
            for j in range(left, right + 1):
                if isPrime(grid[top][j]):
                    res.append(grid[top][j])
            top += 1

            # 2. 从上到下遍历右列
            for i in range(top, bottom + 1):
                if isPrime(grid[i][right]):
                    res.append(grid[i][right])
            right -= 1

            # 3. 从右到左遍历底行（确保当前还有未遍历的行）
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if isPrime(grid[bottom][j]):
                        res.append(grid[bottom][j])
                bottom -= 1

            # 4. 从下到上遍历左列（确保当前还有未遍历的列）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if isPrime(grid[i][left]):
                        res.append(grid[i][left])
                left += 1

        return res