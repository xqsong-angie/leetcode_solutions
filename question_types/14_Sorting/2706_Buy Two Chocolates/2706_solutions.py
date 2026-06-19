#20260618
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count=[0]*100
        n=len(prices)
        for i in range(n):
            count[prices[i]-1]+=1
        res=[]
        for i in range(100):
            res.extend([i+1]*count[i])
        if money-res[0]-res[1]<0:
            return money
        else:
            return money-res[0]-res[1]