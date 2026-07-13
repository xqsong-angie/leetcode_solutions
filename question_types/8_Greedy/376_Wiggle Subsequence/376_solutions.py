class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:#==1
            return 1
        else:
            cnt=1
            prev_diff=0#保存上一个diff
            for i in range(1,len(nums)):
                cur_diff=nums[i]-nums[i-1]
                if prev_diff<=0 and cur_diff>0 or prev_diff>=0 and cur_diff<0:#因为cur_diff才是真实的，而cur_diff是绝对不能等于0的，所以不会遇到前后相等的被算进去了，prev_diff==0只可能是开头的占位符
                    cnt+=1
                    prev_diff=cur_diff
        return cnt
    
#20260712 看了一遍