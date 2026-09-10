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
            if i > 0 and nums[i] == nums[i-1]:#值去重
                continue
            
            seen = set() #
            j = i + 1
            while j < len(nums):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], target, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1          # 值去重
                seen.add(nums[j])#nums[j]暂时不能与nums[i]构成solution
                j += 1
        return res

#20260709看了一遍

#20260802
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        res=[]
        hash_map=defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                hash_map[nums[i]+nums[j]].append([i,j])
        
        for i in range(n):
            if -nums[i] in hash_map:
                for h in hash_map[-nums[i]]:
                    if i not in h:
                        path=[nums[i],nums[h[0]],nums[h[1]]]
                        path.sort()
                        if path not in res: #🔥这里超时了 O（n^3) 但是list<list>不能转化为set
                            res.append(path)
        return res
        
