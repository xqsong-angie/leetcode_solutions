class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #f[x] is the total cost to go to the xth step
        #trivial cases
        n=len(cost)#🔥cost[i] 是踏上第 i 级台阶时需要支付的费用，一旦付了钱，就有权从这里出发，向上跳 1 步或 2 步
        f=[0]*(n+3)

        f[0]=0
        f[1]=0

        #trainsition function
        
        for i in range(2,n+1):
            f[i]=min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])

        return f[n]#这是一个虚构的终点，它在台阶 2 的上面，楼顶是n的位置
    
#20260712 看了一遍