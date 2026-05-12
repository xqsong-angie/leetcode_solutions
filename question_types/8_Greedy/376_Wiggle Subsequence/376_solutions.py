class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 1
        else:
            cnt=1
            prev_diff=0
            for i in range(1,len(nums)):
                cur_diff=nums[i]-nums[i-1]
                if prev_diff<=0 and cur_diff>0 or prev_diff>=0 and cur_diff<0:
                    cnt+=1
                    prev_diff=cur_diff
        return cnt