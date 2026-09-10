class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow=0
        fast=0
        n=len(nums)
        while fast<n:
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            else:#nums[fast]==val
                fast+=1
        return slow

#20260523（这一版更符合直觉）                
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #可以考虑成前面是空的，然后补充所有发现!=val的元素
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i