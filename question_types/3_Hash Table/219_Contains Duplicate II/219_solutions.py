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