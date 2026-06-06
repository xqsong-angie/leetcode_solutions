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

#20260605

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            seen = set()
            j = i + 1
            while j < len(nums):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], target, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1          # 跳过重复的 j
                seen.add(nums[j])
                j += 1
        return res
