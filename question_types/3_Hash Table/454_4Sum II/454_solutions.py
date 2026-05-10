class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        mydict={}
        count=0
        for i in range(n):
            for j in range(n):
                if nums1[i]+nums2[j] not in mydict.keys():
                    mydict[nums1[i]+nums2[j]]=0
                mydict[nums1[i]+nums2[j]]+=1

        for k in range(n):
            for l in range(n):
                target=0-(nums3[k]+nums4[l])
                if target in mydict.keys():
                    count+=mydict[target]
        return count