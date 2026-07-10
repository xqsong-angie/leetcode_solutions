#20260707
#https://algo.monster/liteproblems/187
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        count=defaultdict(int)
        res=[]
        for i in range(n-10+1):
            count[s[i:i+10]]+=1
            if count[s[i:i+10]]==2:
                res.append(s[i:i+10])
        return res
    
#20260709 看了一遍