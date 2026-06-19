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

#20260615
#quick sort
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # 1. 随机选取 Pivot
        pivot = random.choice(nums)
        
        # 2. 将数组分为三部分：小于、等于、大于
        # 这样处理可以完美避开“pivot 交换”时产生的逻辑死锁
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        # 3. 递归排序并拼接
        return self.sortArray(left) + mid + self.sortArray(right)
#需要补充原地交换的写法

#bucket sort
#错：
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #bucket
        count=[0]*10**5 #index out of range,少算了一个坑位
        n=len(nums)
        for i in range(n):
            count[nums[i]+5*10**4]+=1
        #sort
        res=[]
        for i in range(10**5):#10**5+1
            res+=[i-5*10**4]*count[i]
        return res
#对：
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #bucket
        count = [0] * (10**5 + 1)
        n=len(nums)
        for i in range(n):
            count[nums[i]+5*10**4]+=1
        #sort
        res=[]
        for i in range(10**5+1):
            res.extend([i-5*10**4]*count[i])
        return res

#20260618   
#heap sort
#https://www.geeksforgeeks.org/dsa/heap-sort/
class Solution:
    # To heapify a subtree rooted with node i
    def heapify(self,arr, n, i):
        # Initialize largest as root 三个指针把数组变树
        largest = i
        # left index = 2*i + 1
        l = 2 * i + 1
        # right index = 2*i + 2
        r = 2 * i + 2
        # If left child is larger than root
        if l < n and arr[l] > arr[largest]:
            largest = l
        # If right child is larger than largest so far
        if r < n and arr[r] > arr[largest]:
            largest = r
        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] #python遵循先求值再赋值原则，可以这么写，其他语言要用swap
            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Build heap (rearrange vector)
        for i in range(n // 2 - 1, -1, -1): #从最右下的那个根节点开始调
            self.heapify(nums, n, i)
        # One by one extract an element from heap
        for i in range(n - 1, 0, -1):
            # Move current root to end
            nums[0], nums[i] = nums[i], nums[0]
            # Call max heapify on the reduced heap
            self.heapify(nums, i, 0)
        return nums
