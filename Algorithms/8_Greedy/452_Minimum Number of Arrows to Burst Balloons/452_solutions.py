class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #找重叠段
        count=1
        points=sorted(points,key=lambda x:(x[0],x[1]))
        n=len(points)
        myrange=points[0][1]#拿到最右位置
        for i in range(1,n):
            x3=points[i][0]#从最小的左位置开始
            x4=points[i][1] 
            if x3>myrange:
                count+=1
                myrange=x4
            else:#x3<=myrange
                myrange=min(myrange,x4)#交集

        return count
    
#20260712 看了一遍
