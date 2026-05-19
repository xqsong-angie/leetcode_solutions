class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_value=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         max_value=max(max_value,prices[j]-prices[i])
        # return max_value
        
        #https://www.youtube.com/watch?v=1pkOgXD63yU

        i=0
        max_num=0
        j=0
        cur=0
        while i<len(prices) and j<len(prices):
            cur=prices[j]-prices[i]
            if cur<0:
                i+=1
            else:
                max_num=max(max_num,prices[j]-prices[i])
                j+=1
        return max_num
                
