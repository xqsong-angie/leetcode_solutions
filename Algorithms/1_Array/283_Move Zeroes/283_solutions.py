#20260725
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=0
        n=len(nums)
        while j<n:
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            j+=1