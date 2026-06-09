#20250923
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

#20260608


from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # 存储的是下标
        
        for i, num in enumerate(nums):
            # 1. 移除已经不在当前窗口左边界内的下标
            if q and q[0] < i - k + 1: #i 为当前窗口末尾idx, i-k+1为当前窗口起始idx(距离当前位置能往左多少)
                q.popleft()
                
            # 2. 维护单调队列：将队列尾部所有小于当前元素的下标弹出
            while q and nums[q[-1]] < num:
                q.pop()
                
            # 3. 将当前下标加入队列
            q.append(i)
            
            # 4. 当窗口大小达到 k 时，开始记录结果（队头永远是当前窗口最大值的下标）
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
