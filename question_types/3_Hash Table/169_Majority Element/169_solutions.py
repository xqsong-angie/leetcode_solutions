#20260727
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        bound=n//2
        counter=Counter(nums)
        for k in counter.keys():
            if counter[k]>bound:
                return k