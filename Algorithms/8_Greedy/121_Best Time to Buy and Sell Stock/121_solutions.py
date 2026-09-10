class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_value=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         max_value=max(max_value,prices[j]-prices[i])
        # return max_value
        
        #https://www.youtube.com/watch?v=1pkOgXD63yU

        i=0
        max_num=0#最大收益，只能买一次卖一次
        j=0
        cur=0
        while i<len(prices) and j<len(prices):
            cur=prices[j]-prices[i]#这里赔了，后面有比这里更低的，那就果断换低的买
            if cur<0:
                i+=1#换低的买
            else:
                max_num=max(max_num,prices[j]-prices[i])#赚了，就更新
                j+=1#一直移动，直到发现一个比当前更低的
        return max_num
                
#20260712 看了一遍