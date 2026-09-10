from heapq import heappop, heappush, heapify
#https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        n=len(nums)
        for i in range(n):
            heappush(heap,-nums[i])
        for i in range(k):
            res=heappop(heap)
        return -res
