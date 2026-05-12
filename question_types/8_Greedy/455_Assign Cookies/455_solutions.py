class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #s: cookie size
        #g: greedy factor of each child
        g.sort()
        s.sort()
        if len(s)==0:
            return 0
        else:
            i=0 
            j=0
            cnt=0
            while i<len(g) and j<len(s):
                if s[j]<g[i]:
                    j+=1
                else:
                    cnt+=1
                    i+=1
                    j+=1

        return cnt