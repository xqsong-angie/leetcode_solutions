class Solution:
    def solution(self,arr):
        n=len(arr)
        res=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if arr[i]>arr[j]>arr[k]:
                        res+=1
        return res
    
#利用乘法原理减到O（N^2)
class Solution:
    def countInversions3(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        
        for j in range(1, n - 1):
            # 统计左侧大于 arr[j] 的个数
            left_greater = 0
            for i in range(j):
                if arr[i] > arr[j]:
                    left_greater += 1
            
            # 统计右侧小于 arr[j] 的个数
            right_smaller = 0
            for k in range(j + 1, n):
                if arr[k] < arr[j]:
                    right_smaller += 1
            
            ans += left_greater * right_smaller
            
        return ans

# 验证 Example 2: {9, 6, 4, 5, 8}
s = Solution()
print(s.countInversions3([9, 6, 4, 5, 8]))  # 输出: 2