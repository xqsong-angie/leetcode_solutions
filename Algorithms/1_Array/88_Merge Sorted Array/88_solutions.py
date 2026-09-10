#20260725
#错：想到也许可以两个数组互换一些值来暂存，或者用heap做归并，但似乎很麻烦
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=j=0
        heap=heapq.heapify([])
        while True:
            if nums1[i]<=nums2[j]:
                i+=1
            else:#nums1[i]>nums2[j]
                if nums2[j+1]>=nums1[i]:
                    nums1[i],nums2[j]=nums1[j],nums2[i]
                else:
                    heap.heappush(nums1[i])
                    nums1[i]=nums2[j]
                    j+=1
                i+=1
#对：逆向双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1 指向 nums1 有效元素的末尾
        # p2 指向 nums2 的末尾
        # p 指向 nums1 的整体末尾（填数的位置）
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # 从后往前遍历，谁大谁就填在 p 位置
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:#🔥最坏情况是nums2所有数都比nums1最大值大，也最多就是占用了所有0的1位置，不会和p指针左边的值冲突
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果 nums2 还有剩余元素，直接拷贝到 nums1 前面
        # （🔥如果是 nums1 剩余，它本来就在正确的位置上，不用管）
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
