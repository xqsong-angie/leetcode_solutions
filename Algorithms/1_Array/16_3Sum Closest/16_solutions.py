#20260725
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff=float('inf')
        n=len(nums)
        res=0
        nums.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target
                elif nums[i]+nums[j]+nums[k]<target:
                    cur_diff=target-(nums[i]+nums[j]+nums[k])
                    if min_diff>cur_diff:
                        min_diff=min(min_diff,cur_diff)
                        res=target-min_diff
                    j+=1
                else:#>target
                    cur_diff=(nums[i]+nums[j]+nums[k])-target
                    if min_diff>cur_diff:
                        min_diff=cur_diff
                        res=min_diff+target
                    k-=1
        return res

            