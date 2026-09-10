#20260726
from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        n=len(costs)
        dp=[[0]*3 for _ in range(n)]
        if n>0:
            dp[0][0]=costs[0][0]
            dp[0][1]=costs[0][1]
            dp[0][2]=costs[0][2]
            for i in range(1,n):
                dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i][0]#第i个房子选红色
                dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i][1]#第i个房子选蓝色
                dp[i][2]=min(dp[i-1][0],dp[i-1][1])+costs[i][2]#第i个房子选绿色
            return min(dp[n-1])
        else:
            return 0