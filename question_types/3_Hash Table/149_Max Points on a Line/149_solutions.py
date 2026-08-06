#20260805
import math

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 0
        
        # 遍历每一个点作为基准点
        for i in range(n):
            slopes = {}
            # 统计通过当前基准点的最多共线点数
            current_max = 0 
            
            # 只需要看 i 后面的点，避免重复计算
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # 利用求最大公约数，将斜率化为最简分数
                # Python 的 math.gcd 可以很好地处理负数和 0 的情况
                g = math.gcd(dx, dy)
                
                # 统一符号：如果分母为负，将负号移到分子上，保证相同的斜率得到完全相同的 key
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slope_key = (dx, dy)
                
                # 存入哈希表
                slopes[slope_key] = slopes.get(slope_key, 0) + 1
                current_max = max(current_max, slopes[slope_key])
            
            # current_max 是与点 i 共线的其他点的最大数量
            # 加上点 i 自己（+1）就是这条线上的总点数
            max_points = max(max_points, current_max + 1)
            
        return max_points