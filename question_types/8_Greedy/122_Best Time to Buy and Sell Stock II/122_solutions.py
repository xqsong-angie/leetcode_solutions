class Solution:
    def maxProfit(self, prices: List[int]) -> int:#可以买卖多次
        maxProfit=0
        if len(prices)==1:#如果只有一天，那就不买
            return 0
        else:
            for i in range(1,len(prices)):
                diff=prices[i]-prices[i-1]#只要有得赚就买卖，把每个空隙能赚差价的都赚了，而且当天卖出去的还能再买回来，如果发现明天更有得赚，毕竟一次能看到整个数组
                if diff>0:
                    maxProfit+=diff
            return maxProfit
            
#20260712 看了一遍