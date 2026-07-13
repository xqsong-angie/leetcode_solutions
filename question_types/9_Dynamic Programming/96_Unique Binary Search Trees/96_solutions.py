class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)#dp[i]为n=i时，bst总数
        dp[0]=1#理论上n=0的时候是空树，有一种
        # i is the number of nodes
        for i in range(1,n+1):
            for j in range(1,i+1): #j as the head，每个数轮流当根
                dp[i]+=dp[j-1]*dp[i-j]#如果根是j, 那么左边有比j小的j-1个节点，右边有i-j个节点， j-1+1+i-j==i,这就是乘法原理和加法原理

        return dp[n]
    
#20260712 看了一遍
