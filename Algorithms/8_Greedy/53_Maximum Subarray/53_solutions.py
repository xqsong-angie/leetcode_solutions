class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=-1 #局部sum
        result=-10**4-1 #全局最大sum
        for i in range(len(nums)):
            if sum<0:#就相当于把前面加和的东西算成一个负数，这个窗口废了，能想到第一个数要从正数开始，就应该想到这一点
                sum=nums[i]
            else:
                sum+=nums[i]#如果是正的就还可以累加
            result=max(sum,result)
                
        return result
    
#20260712 看了一遍