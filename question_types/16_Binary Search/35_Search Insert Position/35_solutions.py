#20260623
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin=0
        end=len(nums)#这里定义为左闭右开
        while begin<end:
            mid=(begin+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                begin=mid+1
            elif nums[mid]>target:
                end=mid#这里用end还是end-1取决于区间定义为左闭右闭还是左闭右开
        return begin

            
