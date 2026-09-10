class Solution:
    def climbStairs(self, n: int) -> int:
        f=[0]*(n+3)
        #trivial case
        f[1]=1
        f[2]=2
        #transition function
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]

