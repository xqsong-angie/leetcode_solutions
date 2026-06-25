#20260623
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin=0
        end=len(nums)
        while begin<end:
            mid=(begin+end)//2
            if nums[mid]==target:
                return mid
            elif nums[begin]>nums[mid]: #mid当前在右区间
                if nums[mid]<target and target<=nums[end-1]:#说明此次循环begin和end呈单调状态，找到单调子区间，且target在此子区间内（也在右区间）,end虽然是开区间，但是nums[end]会index out of range
                    begin=mid+1 #就可以把begin挤到右区间来了，可以开始用常规二分
                else:
                    end=mid#target掉进不单调的左半了，砍掉没有target的那半
            elif nums[begin]<=nums[mid]:#mid在左区间(注意左边是闭区间，用<=)
                if nums[begin]<=target and target<nums[mid]: #此次循环进入单调区间，且target在子区间内（也在左区间）
                    end=mid
                else:
                    begin=mid+1##target掉进不单调的右半了，砍掉没有target的那半
        return -1
            
"""
所以它这个就是说，因为二分查找只能用在单调递增区间，所以我们要先保证我们在单调区间上搜索。
然而有时候倒霉，target恰好掉进不单调的那一半了。我们这时候还不能开始二分查找，只能进一步缩小范围。
然后把这半不单调的，当作另一个被rotate过了的数组重新开始处理。直到找到一个target在的单调区间，
因为target必然在其中一段上。
"""
