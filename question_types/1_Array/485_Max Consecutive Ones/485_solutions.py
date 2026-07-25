#20260725
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt=0
        cur_cnt=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=1:
                max_cnt=max(max_cnt,cur_cnt)
                cur_cnt=0
            else:
                cur_cnt+=1
        max_cnt=max(max_cnt,cur_cnt)
        return max_cnt