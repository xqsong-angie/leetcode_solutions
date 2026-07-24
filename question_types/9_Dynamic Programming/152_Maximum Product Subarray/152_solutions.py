#20260719
#错：无法处理两个负数相乘的情况
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp=nums
        n=len(nums)
        for i in range(1,n):
            dp[i]=max(nums[i]*dp[i-1],dp[i])
        return max(dp)
    
#对：不但要保存最大值，还要保存“最小负值”
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # 初始化：当前的最小值、最大值和最终结果都设为第一个元素
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 如果当前数是负数，最大值和最小值会互换，先把旧的 curr_max 存起来
            temp_max = curr_max
            
            # 核心状态转移方程：比较 (当前元素本身, 乘以之前最大值, 乘以之前最小值)
            curr_max = max(num, num * temp_max, num * curr_min)
            curr_min = min(num, num * temp_max, num * curr_min)
            
            # 更新全局最大乘积
            res = max(res, curr_max)
            
        return res
