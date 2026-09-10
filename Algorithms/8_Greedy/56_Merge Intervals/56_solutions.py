class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x: (x[0],x[1]))
        n=len(intervals)
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for i in range(1,n):
            if intervals[i][0]>end:
                res.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            else:
                end=max(end,intervals[i][1])
        res.append([start,end])
            
        return res