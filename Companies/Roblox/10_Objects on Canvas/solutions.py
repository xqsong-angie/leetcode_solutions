#20260823
#错
class Solution:
    def solution(self,centers): #centers: [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
        n=len(centers)
        ans=0
        for i in range(n-1):
            for j in range(1,n):#🔥从i+1开始
                x1=centers[i][0]
                y1=centers[i][1]
                x2=centers[j][0]
                y2=centers[j][1]
                if abs(x1-x2)<= 2 and abs(y1-y2)<= 2:
                    ans+=1
        return ans
    
#对：
class Solution:
    def solution(self,centers): #centers: [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
        n=len(centers)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                x1=centers[i][0]
                y1=centers[i][1]
                x2=centers[j][0]
                y2=centers[j][1]
                if abs(x1-x2)<= 2 and abs(y1-y2)<= 2:
                    ans+=1
        return ans

#哈希：
from collections import defaultdict
class Solution:
    def solution(self, centers: list[list[int]]) -> int:
        # 用字典记录每个坐标上的物体数量 (x, y) -> count
        point_counts = defaultdict(int)
        for x, y in centers:
            point_counts[(x, y)] += 1
            
        ans = 0
        
        # 遍历所有出现过的位置
        points = list(point_counts.keys())
        m = len(points)
        
        for i in range(m):
            x1, y1 = points[i]
            count1 = point_counts[(x1, y1)] #🔥(x1, y1)出现过的次数
            
            # 1. 同一坐标上的物体互相碰撞（组合公式 C(count1, 2)）
            if count1 > 1:
                ans += count1 * (count1 - 1) // 2
                
            # 2. 与附近其他坐标上的物体碰撞
            for j in range(i + 1, m):
                x2, y2 = points[j]
                
                # 剪枝：如果 x 轴距离已经 > 2，不需要进一步计算
                if abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
                    count2 = point_counts[(x2, y2)]
                    ans += count1 * count2
                    
        return ans
        