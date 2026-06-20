#20260619
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_ori=list(heights)
        heights.sort()
        count=0
        for i in range(len(heights)):
            if heights_ori[i]!=heights[i]:
                count+=1
        return count