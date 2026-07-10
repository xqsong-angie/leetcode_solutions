class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        count=0 #记录现在应该填的数字
        start_x=0#表示行起始位
        start_y=0#表示列起始位
        offset=1#一开始就是要剩一个，用来拐弯
        loop=n//2#说明offset到哪里停止，两边到达中心的位置了
        while offset <=loop:
            #top（最上面未填行，列移动）从左到右，正循环
            for j in range(start_y,n-offset):
                count+=1#先增加到当前要填数的大小
                res[start_x][j]=count#填入，列移动
            
            #right（最右侧未填列，行移动）从上到下，正循环
            for i in range(start_x,n-offset):
                count+=1
                res[i][n-offset]=count#行移动

            #bottom（最下面未填行，列移动）从右到左，负循环
            for j in range(n-offset,start_y,-1):
                count+=1
                res[n-offset][j]=count#列移动

            #left（最左侧未填列，行移动）从下到上，负循环
            for i in range(n-offset,start_x,-1):
                count+=1
                res[i][start_y]=count#行移动

            start_x+=1
            start_y+=1
            offset+=1

        if n%2!=0:#奇数比偶数多个芯
            count+=1
            res[n//2][n//2]=count #中心位置

        return res

