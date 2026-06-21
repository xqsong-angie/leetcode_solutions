#20250619
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        while j<len(nums)-1:
            if nums[j+1]==nums[j]:
                j+=1
            else:#nums[j+1]!=nums[j]
                nums[i+1]=nums[j+1]
                i+=1
                j+=1

        k=i+1
        return k

#20260620
