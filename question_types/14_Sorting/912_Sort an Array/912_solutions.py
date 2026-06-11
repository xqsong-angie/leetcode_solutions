#20260605
#bubble sort (leetcode都是跑不过O(n^2)的，需要O(nlogn)
# class Solution:
#     #bubble sort
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         for _ in range(n):
#             for i in range(n-1):
#                 if nums[i]>nums[i+1]:
#                     temp=nums[i]
#                     nums[i]=nums[i+1]
#                     nums[i+1]=temp
#         return nums
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            # 优化 1：n - i - 1，后面已经排好序的部分不用再比了
            for j in range(0, n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] # Python 特色简写，省去 temp
                    swapped = True
            
            # 优化 2：如果某一轮走完，发现一次交换都没发生，说明数组已经有序了，直接退出
            if not swapped:
                break
        return nums
