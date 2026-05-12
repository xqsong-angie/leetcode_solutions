class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #找重叠段
        count=1
        points=sorted(points,key=lambda x:(x[0],x[1]))
        n=len(points)
        myrange=points[0][1]
        for i in range(1,n):
            x1=points[i-1][0]
            x2=points[i-1][1]
            x3=points[i][0]
            x4=points[i][1] 
            if x3>myrange:
                count+=1
                myrange=x4
            else:
                if myrange<x3:
                    count+=1
                myrange=min(myrange,x4)

        return count