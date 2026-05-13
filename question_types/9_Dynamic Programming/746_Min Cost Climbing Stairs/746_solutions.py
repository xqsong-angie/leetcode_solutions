class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #f[x] is the total cost to go to the xth step
        #trivial cases
        n=len(cost)
        f=[0]*(n+3)

        f[0]=0
        f[1]=0

        #trainsition function
        
        for i in range(2,n+1):
            f[i]=min(f[i-1]+cost[i-1],f[i-2]+cost[i-2])

        return f[n]