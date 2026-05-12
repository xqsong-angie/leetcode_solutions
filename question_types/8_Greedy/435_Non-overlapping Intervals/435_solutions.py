class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals=sorted(intervals,key=lambda x:(x[0],x[1]))
        cnt=0
        myrange=intervals[0][1]
        for i in range(1,n):
            x1=intervals[i][0]
            x2=intervals[i][1]
            if x1>=myrange:
                myrange=x2
            else:
                cnt+=1
                myrange=min(myrange,x2)
        return cnt