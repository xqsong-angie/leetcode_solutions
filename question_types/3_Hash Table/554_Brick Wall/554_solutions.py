#20260709
#错：无法应对wall=[[1],[1],[1]], output=3的情况
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sum=[]
        for i in range(len(wall)):
            path=[]
            path_sum=0
            for j in range(len(wall[i])):
                path_sum+=wall[i][j]
                path.append(path_sum)
            prefix_sum.append(path)
        counter=defaultdict(int)
        for i in range(len(prefix_sum)):
            for j in range(len(prefix_sum[i])):
                counter[prefix_sum[i][j]]+=1

        counter[sum(wall[0])]=0
        cut = max(counter, key=counter.get) #https://www.geeksforgeeks.org/python/python-get-key-with-maximum-value-in-dictionary/
        res=0
        for i in range(len(prefix_sum)):
            if cut not in prefix_sum[i]:
                res+=1
        return res
#对：
from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counter = defaultdict(int)
        
        for row in wall:
            path_sum = 0
            # 🔥len(row) - 1 确保了我们不把最右侧的墙边界算作“砖缝”
            for j in range(len(row) - 1):
                path_sum += row[j]
                counter[path_sum] += 1
        
        # 如果 counter 为空（比如 [[1],[1],[1]] 内部没有任何缝隙），说明最大缝隙数是 0
        max_gaps = max(counter.values()) if counter else 0
        
        # 最终结果 = 总行数 - 最大缝隙数
        return len(wall) - max_gaps