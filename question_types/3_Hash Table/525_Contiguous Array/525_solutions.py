#20250707
#https://algo.monster/liteproblems/525
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        idx_map={} 
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
               nums[i]=-1 #先把所有0都转化为-1就可以用前缀和了
        prefix_sum=0
        prefix_sums=[]
        max_length=0
        for i in range(n):
            prefix_sum+=nums[i]
            prefix_sums.append(prefix_sum) #构建前缀和函数

        for i in range(n):
            if  prefix_sums[i]==0: #为0的位置单独处理，自然就是相等位置
                max_length=max(max_length,i+1)
            elif prefix_sums[i] in idx_map.keys():#不为0的位置，要和前面算差
                max_length=max(max_length,i-idx_map[prefix_sums[i]])
            else:
                idx_map[prefix_sums[i]]=i#记录最远的i, 如果是最近还要不断更新

        return max_length
                
#20260709 看了一遍

