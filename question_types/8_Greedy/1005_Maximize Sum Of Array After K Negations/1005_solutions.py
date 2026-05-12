class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        flag=True
        while flag==True and k>0:
            flag=False
            idx=-1
            largest_neg=0
            for i in range(len(nums)):
                if nums[i]<0:
                    flag=True
                    if largest_neg==0:
                        largest_neg=-nums[i]
                        idx=i
                    else:
                        if largest_neg<-nums[i]:
                            largest_neg=-nums[i]
                            idx=i

            if idx>=0:
                nums[idx]=-nums[idx]
                k-=1

        if k>0:
            nums.sort()
            if k%2==0: #even
                return sum(nums)
            else:#odd
                return sum(nums)-2*nums[0]
        elif k==0:
            return sum(nums)
