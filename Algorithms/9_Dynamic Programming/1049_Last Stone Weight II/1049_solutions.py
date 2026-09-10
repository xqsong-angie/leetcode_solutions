class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum=sum(stones)
        target=stone_sum//2

        dp=[0]*(target+1)
        for i in range(len(stones)):
            for j in range(target,stones[i]-1,-1):
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        return abs((stone_sum-dp[target])-dp[target])#石头相撞问题，本质上表达式是一堆石头撞另一堆石头的形式，所以可以用partition equal subset sum 解决
                
#20260712 看了一遍