class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #s: cookie size
        #g: greedy factor of each child
        g.sort()#从最小的孩子开始满足，这样可以多满足一些
        s.sort()#尽量先把小饼干发出去
        if len(s)==0:#没有饼干
            return 0#那没办法
        else:#有饼干
            i=0 
            j=0
            cnt=0#满足的孩子个数
            while i<len(g) and j<len(s):
                if s[j]<g[i]:#当前饼干满足不了当前孩子
                    j+=1#再换一个大的试试
                else:#能满足，就不要换了
                    cnt+=1#满足了一个孩子
                    i+=1#当前孩子已经被满足了，看下一个没满足的孩子
                    j+=1#当前饼干已经被发出去了，不能再用了，换下一块饼干

        return cnt

#20260712 看了一遍