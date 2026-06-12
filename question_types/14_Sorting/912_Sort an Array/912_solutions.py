#20260610
#bubble sort (leetcode都是跑不过O(n^2)的，需要O(nlogn)
# class Solution:
#     #bubble sort
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         for _ in range(n):
#             for i in range(n-1):
#                 if nums[i]>nums[i+1]:
#                     temp=nums[i]
#                     nums[i]=nums[i+1]
#                     nums[i+1]=temp
#         return nums
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            # 优化 1：n - i - 1，后面已经排好序的部分不用再比了
            for j in range(0, n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] # Python 特色简写，省去 temp
                    swapped = True
            
            # 优化 2：如果某一轮走完，发现一次交换都没发生，说明数组已经有序了，直接退出
            if not swapped:
                break
        return nums
    

#20260611
#错：
class Solution:
    #insertion sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            temp=nums[i]
            j=i
            while j>0:
                if temp<nums[j]: #！！！这里只执行了一次，因为j=i, temp=nums[j]，直接break了
                    nums[j]=nums[j-1]
                    j-=1
                else:
                    break
            nums[j]=temp
        return nums
    
#正确：
class Solution:
    #insertion sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            temp=nums[i]
            j=i
            while j>0 and temp<nums[j-1]: #和左侧的做比较
                nums[j]=nums[j-1]
                j-=1
            nums[j]=temp
        return nums

#selection sort
#错：
class Solution:
    #selection sort
    #https://www.w3schools.com/python/ref_list_index.asp
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            min_val=min(nums[i:])
            min_idx=nums[i:].index(min_val) #index是按照切片后的新数组返回索引，会错位
            nums[min_idx]=nums[i]
            nums[i]=min_val
        return nums

#正确：
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_idx = i  # 记录当前未排序部分最小值的索引 （不依赖.index找索引，手动更新索引）
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j  # 发现更小的，更新索引
            
            # 将未排序部分的最小值与当前位置 i 交换
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
    
#merge sort
class Solution:
    #merge sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if not nums:
            return 
        elif n==1:
            return nums
        elif n==2:
            if nums[0]<nums[1]:
                return nums
            else:
                return [nums[1],nums[0]]
        else:
            split=n//2
            left=self.sortArray(nums[:split]) #split别+1
            right=self.sortArray(nums[split:])
            res=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
                    
            res+=left[i:] #注意别忘了补齐
            res+=right[j:]
            return res
