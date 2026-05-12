class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        if len(prices)==1:
            return 0
        else:
            for i in range(1,len(prices)):
                diff=prices[i]-prices[i-1]
                if diff>0:
                    maxProfit+=diff
            return maxProfit
            
