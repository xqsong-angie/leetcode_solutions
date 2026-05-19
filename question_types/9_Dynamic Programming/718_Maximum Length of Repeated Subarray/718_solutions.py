class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        dp=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
        return max(max(x) for x in dp)