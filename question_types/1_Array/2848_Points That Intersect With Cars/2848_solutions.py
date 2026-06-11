#20260610
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        visited=[0]*(100+1)
        n=len(nums)
        for i in range(n):
            for j in range(nums[i][0],nums[i][1]+1):
                visited[j]=1

        cnt=0
        for i in range(101):
            if visited[i]==1:
                cnt+=1
        return cnt