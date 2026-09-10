#20260704
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() 
        low=0 #low, high代表连续区间
        high=len(nums)
        while low<=high:
            mid=(low+high)//2
            if 0<=mid<=len(nums)-1:
                if mid==nums[mid]:#说明missing在mid右侧,左边都是连续的
                    low=mid+1
                else:#说明在mid左侧，说明左边就已经断掉了
                    high=mid-1
            else:
                return mid
        #左边的idx与数值一一对应，missing右边的不再一一对应，找到missing idx即可
        return low
    
#20260724 看了一遍