class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        my_sums=sum(nums)
        
        if (my_sums-target)%2!=0:
            return 0
        else:
            pack_minus=(my_sums-target)//2
            pack_plus=pack_minus+target
            if pack_plus<0 or pack_minus<0:
                return 0
            else:
                dp=[0]*(pack_plus+1)
                dp[0]=1
                for i in range(len(nums)):
                    for j in range(pack_plus,nums[i]-1,-1): 
                        dp[j]+=dp[j-nums[i]]

                    
                return dp[pack_plus]
