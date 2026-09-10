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

#20260803
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=[]
        seen=defaultdict(int)#count
        for i in range(len(s)-9):
            myslice=s[i:i+10]
            if myslice in seen and seen[myslice]==1:
                res.append(myslice)
            seen[myslice]+=1
        return res
