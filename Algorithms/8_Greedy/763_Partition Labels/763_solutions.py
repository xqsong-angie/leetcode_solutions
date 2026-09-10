class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        myhash={}
        farthest_pos=[]
        res=[]
        n=len(s)
        for i in range(n):
            myhash[s[i]]=i#这样得到的是每个字母对应最远端的index
        for i in range(n):
            farthest_pos.append(myhash[s[i]])#把每一个字母都代替成字母所对应的最远位置的索引

        i=0
        pos=farthest_pos[0]
        last_end=-1
        while i<=pos:
            if i==pos:#就说明没到切割位
                if not res:
                    res.append(pos+1)#第一段长度
                    last_end=pos#第一段最后一个的位置
                else:
                    res.append(pos-last_end)#之后段的长度
                    last_end=pos#之后段最后一个的位置
            if i<n-1:#没有到最后一个
                i+=1
                pos=max(pos,farthest_pos[i])#直到把大家都包进去了
            else:
                break
        return res

#20260712 看了一遍