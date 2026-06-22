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

#20260621
#错：
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=k=0
        n=len(nums)
        cnt=0
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                j=i
                cnt+=1
            elif nums[i]!=nums[i-1]: #i=0时，直接进入这里，变成nums[-1]，逻辑混乱
                k=i-1
                nums[j]+=nums[i]
                j+=1
                if j==k:
                    continue
        return len(nums) #这里把后面重复的也算上了
