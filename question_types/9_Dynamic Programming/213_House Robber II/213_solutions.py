#20250723

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        f=[[0]*(n+3) for i in range(2)]
        f[0][1]=0#not choosing nums[0]
        f[1][1]=nums[0]

        if n==1:
            return max(f[0][1],f[1][1])
        else:
            f[0][2]=nums[1]
            f[1][2]=nums[0] #choose nums[0]

            for i in range(3, n+1):
                f[0][i]=max(f[0][i-1],f[0][i-2]+nums[i-1])
            
            for i in range(3,n):
                f[1][i]=max(f[1][i-1],f[1][i-2]+nums[i-1])

            return max(f[0][n],f[1][n-1])

#20250823

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        elif n>=3:
            def max_money(mylist):
                n=len(mylist)
                dp=[0]*n
                dp[0]=mylist[0]
                dp[1]=max(mylist[0],mylist[1])
                for i in range(2,n):
                    dp[i]=max(dp[i-1],dp[i-2]+mylist[i])
                return dp[n-1]
            return max(max_money(nums[1:]),max_money(nums[:-1]))
        