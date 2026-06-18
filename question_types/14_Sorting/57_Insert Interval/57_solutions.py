#20260616
#错：
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #https://algo.monster/liteproblems/57
        #insert
        intervals_sorted=[]
        i=0
        n=len(intervals)
        while i<n: #sort by start time
            if intervals[i][0]<=newInterval[0]:
                intervals_sorted.append(intervals[i])
                i+=1
            else:
                intervals_sorted.append(newInterval)

        #merge
        res=[]
        for i in range(n+1):
            if i==0:
                res.append(intervals_sorted[0])
            else:
                if intervals_sorted[i][0]<=intervals_sorted[i-1][1]:
                    res[-1]=[intervals_sorted[i-1][0],max(intervals_sorted[i][1],intervals_sorted[i-1][1])]
                else:
                    res.append(intervals_sorted[i])
        return res
    
#对：

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
            
        # 1. 按照起点顺序插入
        intervals_sorted = []
        i = 0
        n = len(intervals)
        flag = False
        
        while i < n:
            if intervals[i][0] <= newInterval[0] or flag == True:
                intervals_sorted.append(intervals[i])
                i += 1
            else:
                intervals_sorted.append(newInterval)
                flag = True
                
        # 修复：如果全进去了都没触发else，说明newInterval是最后一个
        if not flag:
            intervals_sorted.append(newInterval)

        # 2. 合并重叠区间
        res = []
        for i in range(len(intervals_sorted)): # 这里直接用正确长度遍历即可
            if not res:
                res.append(intervals_sorted[i])
            else:
                # 如果当前区间的起点 <= 结果集中最后一个区间的终点，说明有重叠
                if intervals_sorted[i][0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], intervals_sorted[i][1])
                else:
                    res.append(intervals_sorted[i])
        return res

#更推荐的写法
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # 1. 处理所有完全在 newInterval 左侧且无交集的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. 处理所有和 newInterval 有交集的区间，更新 newInterval
        # 有交集的条件：当前区间的起点 <= 新区间的终点
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0]) 
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 将合并后的新区间加入结果
        res.append(newInterval)
        
        # 3. 处理所有完全在 newInterval 右侧的区间
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res