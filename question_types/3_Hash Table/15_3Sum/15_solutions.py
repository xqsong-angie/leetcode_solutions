#two pointer solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]==-nums[i]:
                    res.append((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>-nums[i]:
                    right-=1
                else:
                    left+=1
        return list(set(res))
