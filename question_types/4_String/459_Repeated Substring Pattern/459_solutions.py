#20250921
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        nxt=[0]*n
        j=0
        for i in range(1,n):
            while j>0 and s[i]!=s[j]:
                j=nxt[j-1]
            if s[i]==s[j]:
                j+=1
            nxt[i]=j
        if nxt[n-1]==0:
            return False
        elif n%(n-nxt[n-1])!=0:
            return False
        else:
            return True
        
#20260606
class Solution:
    #https://algo.monster/liteproblems/459
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)
