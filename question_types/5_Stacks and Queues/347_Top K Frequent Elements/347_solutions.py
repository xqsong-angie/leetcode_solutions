class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for i in range(len(nums)):
            if nums[i] not in mydict.keys():
                mydict[nums[i]]=0
            else:
                mydict[nums[i]]+=1
        mydict_sorted=sorted(mydict.items(), key=lambda item: item[1], reverse=True)
        res=[]
        for mk,v in mydict_sorted:
            if len(res)<k:
                res.append(mk)
            else:
                break
        return res


