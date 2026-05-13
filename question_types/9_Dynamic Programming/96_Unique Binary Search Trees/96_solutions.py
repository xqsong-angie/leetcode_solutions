class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        # i is the number of nodes
        for i in range(1,n+1):
            for j in range(1,i+1): #j as the head
                dp[i]+=dp[j-1]*dp[i-j]

        return dp[n]