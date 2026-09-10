class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[j] is the longest substring can be matched from the beginning 完全背包变形题，注意是排列题！
        dp=[0]*(len(s)+1)
        dp[0]=0
        for j in range(1,len(s)+1):
            for i in range(len(wordDict)):
                if j>=len(wordDict[i]) and s[:j].endswith(wordDict[i]): #加限制
                    dp[j]=max(dp[j],dp[j-len(wordDict[i])]+len(wordDict[i]))

        if dp[len(s)]==len(s):
            return True
        else:
            return False
                    
#20260717 看了一遍 