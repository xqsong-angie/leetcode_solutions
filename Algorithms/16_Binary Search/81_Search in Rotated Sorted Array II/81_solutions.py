#20260727
#错：
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=target<=nums[high]:#target在单调区间 🔥[3, 1, 3]满足但不单调
                #开始二分查找
                if target==nums[mid]:
                    return True
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]<=nums[low]<=target:#target在左非单调区间
                high=mid-1#只能缩区间，不能二分🔥缩区间过于激进，会把target直接砍掉
            elif target<=nums[high]<=nums[low]:#target在右非单调区间
                low=mid+1#只能缩区间，不能二分
            else:
                break
        return False
    
#对：
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
    
        while low <= high:
            mid = (low + high) // 2
            
            # 找到目标值
            if nums[mid] == target:
                return True
            
            # 🔥关键点：遇到三者相等，无法判断哪边有序，温和地缩小两端边界
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            # 左半边是有序的
            elif nums[low] <= nums[mid]:
                # target 是否落在左半边有序区间内
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            # 右半边是有序的
            else:
                # target 是否落在右半边有序区间内
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False