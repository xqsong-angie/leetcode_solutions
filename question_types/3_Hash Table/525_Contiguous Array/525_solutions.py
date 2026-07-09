#20250707
#https://algo.monster/liteproblems/525
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        idx_map={} 
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
               nums[i]=-1
        prefix_sum=0
        prefix_sums=[]
        max_length=0
        for i in range(n):
            prefix_sum+=nums[i]
            prefix_sums.append(prefix_sum)

        for i in range(n):
            if  prefix_sums[i]==0:
                max_length=max(max_length,i+1)
            elif prefix_sums[i] in idx_map.keys():
                max_length=max(max_length,i-idx_map[prefix_sums[i]])
            else:
                idx_map[prefix_sums[i]]=i

        return max_length
                

