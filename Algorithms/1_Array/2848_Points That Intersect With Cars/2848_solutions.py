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
    
#20260707
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        stack=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            if nums[i][0]<=stack[-1][1]:
                prev=stack.pop()
                stack.append([prev[0],max(nums[i][1],prev[1])])
            else:
                stack.append(nums[i])
        ans=0
        for i in range(len(stack)):
            ans+=stack[i][1]-stack[i][0]+1
        return ans
    
#20260724
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)
        if n==0:
            return 0
        else:
            while i<n and nums[i]!=val:
                i+=1
            j=i
            while j<n:
                if nums[j]!=val:
                    nums[i]=nums[j]
                    i+=1
                    j+=1
                else:
                    j+=1
            return i