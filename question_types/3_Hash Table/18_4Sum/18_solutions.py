class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for k in range(n-3):
            for i in range(k+1,n-1):
                left=i+1
                right=n-1
                if nums[k]>=0 and target>=0 and nums[k]>target:
                    break
                else:
                    while left<right:
                        if nums[k]+nums[i]+nums[left]+nums[right]==target:
                            res.append((nums[k],nums[i],nums[left],nums[right]))
                            left+=1
                            right-=1
                        elif nums[k]+nums[i]+nums[left]+nums[right]<target:
                            left+=1
                        else:
                            right-=1
        return list(set(res))
                    

                