class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        count=[0]*100
        n=len(nums)
        for i in range(n):
            count[nums[i]-1]+=1
        res=[]
        for i in range(100):
            res.extend([i+1]*count[i])
        missing=[]
        for i in range(n):
            if i>0 and res[i]-res[i-1]>=1:
                for j in range(1,res[i]-res[i-1]):
                    missing.append(res[i-1]+j)
        return missing