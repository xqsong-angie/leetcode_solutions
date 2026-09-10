#20260727
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        first_bad=n
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid):
                first_bad=min(mid,first_bad)
                high=mid-1
            else:
                low=mid+1
        return first_bad
