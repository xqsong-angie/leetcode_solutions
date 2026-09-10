#20260704
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num
        while low<=high:
            mid=(low+high)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                high=mid-1
            else:
                low=mid+1
        return False
