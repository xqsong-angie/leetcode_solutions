class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        middle=(left+right)//2
        while left<=right:
            if target==nums[middle]:
                return middle
            elif target>nums[middle]:
                left=middle+1
                middle=(left+right)//2
            elif target<nums[middle]:
                right=middle-1
                middle=(left+right)//2
        return -1