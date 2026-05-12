class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=-1 #局部sum
        result=-10**4-1 #全局最大sum
        for i in range(len(nums)):
            if sum<0:
                sum=nums[i]
            else:
                sum+=nums[i]
            result=max(sum,result)
                
        return result