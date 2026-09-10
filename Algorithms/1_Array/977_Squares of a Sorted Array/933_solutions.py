class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        j=n-1
        k=n-1
        res=[0]*(n)
        while i<=j:
            if nums[i]**2<=nums[j]**2:
                res[k]=nums[j]**2
                j-=1
                k-=1
            else:
                res[k]=nums[i]**2
                i+=1
                k-=1
        return res
