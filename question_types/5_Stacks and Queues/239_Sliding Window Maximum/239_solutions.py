class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        mydeque=[]
        if n*k==0:
            return []
        elif n<=k:
            res.append(max(nums))
        else:
            for i in range(n):
                if not mydeque:
                    mydeque.append(i)
                else:
                    if nums[i]<=nums[mydeque[-1]]:
                        mydeque.append(i)
                    else:
                        while mydeque and nums[i]>nums[mydeque[-1]]:
                            mydeque.pop()
                        mydeque.append(i)
                if i>=k-1:
                    res.append(nums[mydeque[0]])
                    if mydeque[0]<=i-k+1:
                        mydeque.pop(0)
                    
        return res

