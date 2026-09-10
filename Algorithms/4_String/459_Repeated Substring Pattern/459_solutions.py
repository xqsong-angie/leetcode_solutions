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
        return (s + s).index(s, 1) < len(s)#https://www.w3schools.com/python/ref_string_index.asp string.index(value, start, end)
#从索引 1 开始找 "abab"，我们会发现早在索引 2 的位置（即第一个周期 $p$ 结束的地方）就已经能再次匹配出完整的 "abab" 了（第一段的尾和第二段的头能拼上）