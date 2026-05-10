class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        count=0
        start_x=0
        start_y=0
        offset=1
        loop=n//2
        while offset <=loop:
            #top
            for j in range(start_y,n-offset):
                count+=1
                res[start_x][j]=count
            
            #right
            for i in range(start_x,n-offset):
                count+=1
                res[i][n-offset]=count

            #bottom
            for j in range(n-offset,start_y,-1):
                count+=1
                res[n-offset][j]=count

            #left
            for i in range(n-offset,start_x,-1):
                count+=1
                res[i][start_y]=count

            start_x+=1
            start_y+=1
            offset+=1

        if n%2!=0:
            count+=1
            res[n//2][n//2]=count

        return res
