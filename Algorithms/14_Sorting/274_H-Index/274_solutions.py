#20260618
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        #bucket sort
        count=[0]*1001
        for i in range(len(citations)):
            count[citations[i]]+=1
        res=[]
        for i in range(1001):
            res.extend([i]*count[i])

        h=0
        for i in range(n): 
            offset=n-i
            h=max(h,min(offset,res[i]))
        return h
