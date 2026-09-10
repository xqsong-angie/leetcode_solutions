#20260707
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx=defaultdict(int)
        n=len(nums)
        for i in range(n):
            if nums[i] not in idx.keys():
                idx[nums[i]]=i
            elif abs(idx[nums[i]]-i)<=k:
                return True
            else:
                idx[nums[i]]=i
        return False
    
#20260726
#错：
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        for i in range(n-k):#n==k的时候没法循环
            for j in range(1,k+1):
                if nums[i+j]==nums[i]:
                    return True
        return False
#对：
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # 外层遍历每一个位置 i
        for i in range(n):
            # 🔥内层只检查 i 之后的 k 个元素，同时确保不超过数组边界 n
            for j in range(i + 1, min(i + k + 1, n)):
                if nums[i] == nums[j]:
                    return True
        return False
    
#20260803
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map={}#idx
        for i in range(len(nums)):
            if nums[i] in hash_map and i-hash_map[nums[i]]<=k:
                return True
            else:
                hash_map[nums[i]]=i
        return False

