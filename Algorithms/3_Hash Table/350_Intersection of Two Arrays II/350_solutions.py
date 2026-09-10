#20260803
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapA=Counter(nums1)
        res=[]
        for i in range(len(nums2)):
            if nums2[i] in mapA and mapA[nums2[i]]>=1:
                res.append(nums2[i])
                mapA[nums2[i]]-=1
        return res