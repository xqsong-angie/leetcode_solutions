#20250920
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
                    

 #20260606               
    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            # https://www.geeksforgeeks.org/dsa/find-four-elements-that-sum-to-a-given-value-set-2/#using-hashing-on3-time-and-on-space
            
            # Initialize a set to store unique 
            # quadruplets as sorted tuples
            res_set = set()
            n = len(nums)

            # Iterate to fix the first two elements
            for i in range(n):
                for j in range(i + 1, n):

                    # Set to track elements seen 
                    # so far for the third loop
                    s = set()

                    # Loop to fix the third element and find the fourth
                    for k in range(j + 1, n):
                        sum_val = nums[i] + nums[j] + nums[k]
                        last = target - sum_val

                        # If the fourth required element is already seen
                        if last in s:
                            curr = sorted([nums[i], nums[j], nums[k], last])
                            res_set.add(tuple(curr))

                        # Add current number to the set for future lookup
                        s.add(nums[k])

            return [list(t) for t in res_set]
        
#20260707
#错：res无法收录结果（这个方法就算改了也会超时）
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashmap=defaultdict(list)
        n=len(nums)
        res=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] in hashmap:
                    hashmap[nums[i]+nums[j]].append([i,j])
                elif target-(nums[i]+nums[j]) in hashmap: #问题在这里：你检查的是 target - (nums[i]+nums[j])，但提取的却是 nums[i]+nums[j]
                    sub=hashmap[nums[i]+nums[j]] #应该写hashmap[target - (nums[i]+nums[j])]
                    for k in range(len(sub)):
                        res.append(sub[k]+[i,j])
                elif nums[i]+nums[j] not in hashmap:
                    hashmap[nums[i]+nums[j]]=[[i,j]]

        return res

#改正版
from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        hashmap = defaultdict(list)
        res_set = set()  # 用于存放去重后的四元组结果
        
        # 外层循环 i 作为当前第二对数的左起点
        for i in range(n):
            
            # 【步骤 1：匹配阶段】
            # 用当前 i 和后面的 j 组成第二对数，去哈希表里找互补的第一对数
            for j in range(i + 1, n):
                current_sum = nums[i] + nums[j]
                complement = target - current_sum
                
                # 修复笔误：应该寻找互补值 complement，而不是当前的 current_sum
                if complement in hashmap:
                    # 核心红利：由于哈希表里只存了完全在 i 之前的组合
                    # 因此取出的 (prev_i, prev_j) 必然满足 prev_j < i，下标绝不冲突！
                    for prev_i, prev_j in hashmap[complement]: #🔥特殊数据会严重退化引发超时，比如所有数都一样，这里hashmap[complement]的大小可能高至O（n^2), 导致整个算法时间复杂度为O(n^4)
                        """
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
                        """
                        # 提取四个数值，排序后放入集合去重
                        quadruplet = sorted([nums[prev_i], nums[prev_j], nums[i], nums[j]])
                        res_set.add(tuple(quadruplet))
            
            # 【步骤 2：延迟写入阶段（大招）】
            # 当以当前 i 为左起点的所有配对检测完后，我们再把所有以 i 为右终点的组合 (k, i) 存入哈希表
            # 这样在下一轮循环（外层指针变成 i+1）时，这些组合才能作为“历史组合”被安全用于匹配
            for k in range(i):
                hashmap[nums[k] + nums[i]].append((k, i))
                
        # 将 set 里的元组转换回列表返回
        return [list(t) for t in res_set]