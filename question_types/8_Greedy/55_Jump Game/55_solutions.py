class Solution:
    def canJump(self, nums: List[int]) -> bool:
        myrange=0 #覆盖范围
        if len(nums)==1:
            return True
        else:
            for i in range(len(nums)-1):
                if i>myrange:
                    return False
                myrange=max(i+nums[i],myrange)
                if myrange>=len(nums)-1:
                    return True
            return False