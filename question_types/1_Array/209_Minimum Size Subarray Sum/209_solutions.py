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

#20260705
#错：
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        else:
            n=len(nums)
            mysum=0
            count=0
            min_cnt=n
            i=j=0
            while j<n-1 and i<=j:
                if mysum<target:
                    mysum+=nums[j]
                    count+=1
                    j+=1
                elif mysum==target:#动i和j的时机不太对，尤其是相等的时候一起动，很容易提前结束循环 
                    min_cnt=min(min_cnt,count)
                    i+=1
                    j+=1
                    mysum+=nums[j]
                    mysum-=nums[i]
                else:#>
                    mysum-=nums[i]
                    i+=1
                    count-=1
            return min_cnt

#对（找的是greater than or equal to ）：
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_cnt = float('inf') # 用无穷大初始化，方便后续用 min() 比较
        left = 0
        current_sum = 0
        
        # right 相当于你的 j，left 相当于你的 i
        for right in range(n):
            current_sum += nums[right] # 1. 右指针主动将元素加入窗口
            
            # 2. 当窗口内的和满足要求（>= target）时，尝试缩小左边界
            while current_sum >= target:
                # 更新最小长度 (当前窗口长度为 right - left + 1)
                min_cnt = min(min_cnt, right - left + 1)
                
                # 左指针指向的元素移出窗口，并让左指针前移
                current_sum -= nums[left]
                left += 1
                
        # 如果 min_cnt 没被更新过，说明整个数组加起来都没达到 target，返回 0
        return min_cnt if min_cnt != float('inf') else 0