#20260624
#错：
import math #https://www.geeksforgeeks.org/python/floor-ceil-function-python/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #二分答案经典题（满足条件的数值）
        left=1 #每小时最少吃一个香蕉
        right=max(piles)#每小时最多吃一堆香蕉，否则速度更快没必要
        n=len(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for i in range(n):
                hours+=math.ceil(piles[i]/mid)
            if hours==h:#！！！不能提前返回
                return mid
            elif hours<h: #说明太快，缩右边界
                right=mid-1
            else:#说明太慢，缩左边界
                left=mid+1
        return mid
#对：
import math #https://www.geeksforgeeks.org/python/floor-ceil-function-python/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #二分答案经典题（满足条件的数值）
        left=1 #每小时最少吃一个香蕉
        right=max(piles)#每小时最多吃一堆香蕉，否则速度更快没必要
        n=len(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for i in range(n):
                hours+=math.ceil(piles[i]/mid)
            if hours<=h: #说明太快，缩右边界（有多个满足值，不能用==h提前返回）
                right=mid-1
            else:#说明太慢，缩左边界
                left=mid+1
        return left#最后区间里有多个满足值，指向最小值

