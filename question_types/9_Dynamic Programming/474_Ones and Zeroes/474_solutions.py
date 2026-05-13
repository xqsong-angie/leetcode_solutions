class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count_list=[]
        for s in strs:
            t=tuple((s.count("0"),s.count("1")))
            count_list.append(t)

        dp=[[0]*(n+1)for _ in range(m+1)]
        dp[0][0]=0

        for k in range(len(strs)):
            for i in range(m,count_list[k][0]-1,-1):
                for j in range(n,count_list[k][1]-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-count_list[k][0]][j-count_list[k][1]]+1)

        return dp[m][n]
