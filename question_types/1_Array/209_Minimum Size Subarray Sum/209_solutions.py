#20250826
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        min_length=math.inf
        if sum(nums)<target:
            return 0
        else:
            s=0
            f=0
            mysum=0
            while f<n:
                if mysum<target:
                    mysum+=nums[f]
                    f+=1
                if mysum>=target:
                    min_length=min(min_length,f-s)
                    mysum-=nums[s]
                    s+=1
                    
            while mysum>=target:
                    min_length=min(min_length,f-s)
                    mysum-=nums[s]
                    s+=1
        return min_length

#20260523
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        cur_sum=0
        min_length=n+1
        if sum(nums)<target:
            return 0
        else:
            while j<n:
                cur_sum+=nums[j]
                while cur_sum>=target:
                    min_length=min(min_length,j-i+1)
                    i+=1
                    cur_sum-=nums[i-1]
                j+=1
        return min_length

            