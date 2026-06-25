#20260623
#错（空间超限度）
class Solution:
    def mySqrt(self, x: int) -> int:
        nums=[i for i in range(x+1)]
        begin=0
        end=len(nums)
        while begin<end:
            mid=(begin+end)//2
            if mid**2==x:
                return nums[mid]
            elif mid**2<x:
                begin=mid+1
            elif mid**2>x:
                end=mid
        return nums[begin]-1
#对：由于下标索引=目标值，可以不用开辟数组
class Solution:
    def mySqrt(self, x: int) -> int:
        begin=0
        end=x+1
        while begin<end:
            mid=(begin+end)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                begin=mid+1
            elif mid**2>x:
                end=mid
        return begin-1