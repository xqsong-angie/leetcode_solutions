class Solution:
    def countSubstrings(self, s: str) -> int:#结果算上重复的，只要起终点下标不一致就行
        n=len(s)
        result=0
        dp=[[False for _ in range(n)] for _ in range(n)]#dp[i][j]代表i到j这一段是不是回文
        for k in range(n):#到k为止
            #无论odd还是even,都从中心向两端扩散
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

#20260718 看了一遍，以上代码可以更简洁