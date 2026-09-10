#20260618
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        count=[0]*201
        #bucket sort
        n=len(nums)
        for i in range(n):
            count[nums[i]+100]+=1
        res=[]
        for i in range(201):
            res.extend([i-100]*count[i])
        return res[-1]+res[-2]-res[0]
        