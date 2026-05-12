class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        myhash={}
        farthest_pos=[]
        res=[]
        n=len(s)
        for i in range(n):
            myhash[s[i]]=i
        for i in range(n):
            farthest_pos.append(myhash[s[i]])

        i=0
        pos=farthest_pos[0]
        last_end=-1
        while i<=pos:
            if i==pos:
                if not res:
                    res.append(pos+1)
                    last_end=pos
                else:
                    res.append(pos-last_end)
                    last_end=pos
            if i<n-1:
                i+=1
                pos=max(pos,farthest_pos[i])
            else:
                break
        return res
