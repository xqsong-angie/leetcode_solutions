#20260616

#bucket sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        count=[0]*3
        for i in range(n):
            count[nums[i]]+=1
        k=0
        for i in range(3):
            for j in range(count[i]):
                nums[k]=i
                k+=1