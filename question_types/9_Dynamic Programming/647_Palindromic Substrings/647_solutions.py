class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        result=0
        dp=[[False for _ in range(n)] for _ in range(n)]
        for k in range(n):
            #odd
            i=j=k
            while i>=0 and j<=n-1:
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                        result+=1
                    elif j-i==1:
                        dp[i][j]=True
                        result+=1
                    elif dp[i+1][j-1]==True:
                        dp[i][j]=True
                        result+=1
                i-=1
                j+=1
                
            #even
            i=k
            j=k+1
            while i>=0 and j<=n-1:
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                        result+=1
                    elif j-i==1:
                        dp[i][j]=True
                        result+=1
                    elif dp[i+1][j-1]==True:
                        dp[i][j]=True
                        result+=1
                i-=1
                j+=1
            
        return result

        