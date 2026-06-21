#20260620
#错（反复调用sum导致超时，切片和sum都是O（N），使得整个算法接近O(N^3))
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=j=0
        n=len(nums)
        max_nums=max(nums)
        while i<=j and j<n:
            if nums[i]<=0:
                i+=1
                if j<i:
                    j=i
            elif sum(nums[i:j+1])<0:
                i+=1
            elif sum(nums[i:j+1])<max_nums:
                j+=1
            elif sum(nums[i:j+1])>=max_nums:
                max_nums=sum(nums[i:j+1])
                j+=1 
        return max_nums
    
#对（two pointers)：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]    # 记录全局最大和
        window_sum = 0       # 记录当前双指针窗口内的和
        
        left = 0
        for right in range(n):
            # 1. 右指针右移，将元素纳入窗口
            window_sum += nums[right]
            
            # 2. 更新最大值（只要当前窗口和更大，就记录下来）
            if window_sum > max_sum:
                max_sum = window_sum
                
            # 3. 核心：当窗口和跌破 0 时，说明这个窗口废了，左指针直接“瞬移”
            if window_sum < 0:
                window_sum = 0   # 清空当前窗口和
                left = right + 1 # 左指针直接跳到下一个位置，准备开启新窗口
                
        return max_sum