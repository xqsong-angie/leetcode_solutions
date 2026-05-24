from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.lo = []  # 最大堆（取负模拟）：存较小的一半
        self.hi = []  # 最小堆：存较大的一半

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)           # push到最大堆（堆顶为最大）
        heappush(self.hi, -heappop(self.lo))  # lo最大值给hi(堆顶为最大值里面的最小)
        if len(self.hi) > len(self.lo):   # 保持lo >= hi
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi): #说明是奇数个
            return -self.lo[0]            # 奇数：lo顶就是中位数
        return (-self.lo[0] + self.hi[0]) / 2  # 偶数：两顶平均


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()