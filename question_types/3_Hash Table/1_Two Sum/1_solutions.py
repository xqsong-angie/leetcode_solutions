class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymatch={}
        res=[]
        for i in range(len(nums)):
            gap=target-nums[i]
            if gap in mymatch.keys() and mymatch[gap]!=i:
                res.append(i)
                res.append(mymatch[gap])
                return res
            mymatch[nums[i]]=i
        return []

