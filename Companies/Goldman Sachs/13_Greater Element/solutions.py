#不会
import bisect
class Solution:
    def firstGreaterElementIndices(self, arr1: list[int], arr2: list[int]) -> list[int]:
        n2 = len(arr2)#🔥arr2 的前 k 个元素里，最大值有没有超过 val

        #arr1=[2,4,3]
        #arr2=[1,3,5,2]

        # 1. 构造前缀最大值数组（天然有序）[1,3,5,5]，为了能二分
        pref_max = [0] * n2
        cur_max = -1
        for i, num in enumerate(arr2):
            cur_max = max(cur_max, num)
            pref_max[i] = cur_max
        
        res = []
        # 2. 对 arr1 中的每个元素在 pref_max 中二分搜索，搜索到要插入到右边的位置就是下一个最大的位置
        for val in arr1:
            # bisect_right 查找第一个 > val 的位置
            idx = bisect.bisect_right(pref_max, val)#https://www.geeksforgeeks.org/python/bisect-algorithm-functions-in-python/
            if idx < n2:#🔥元素不存在，bisect_right与bisect_left作用相同，存在时，bisect_right找的是a[i] > x而bisect_left找的是a[i] >= x的
                res.append(idx)
            else:
                res.append(-1)
                
        return res