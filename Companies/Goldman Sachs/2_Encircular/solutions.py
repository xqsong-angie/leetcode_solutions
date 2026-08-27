#不会
class Solution:
    def doesCircleExist(commands: list[str]) -> list[str]:#input是一组测试指令["GGLLGG", "GG", "R"]，output对每条指令判断yes/no
        #机器人会把这一串指令（比如 "RGG"）不间断地重复执行无数遍
        #形成闭环（YES）：比如指令是 "RG"，重复执行几遍后，机器人会在同一个小区域里像转圈圈一样不断重复走过的路线，永远走不出这个圈。
        #跑向无穷远（NO）：比如指令是 "GG"，机器人每一轮都向前走两步且方向不变，重复无限次后，它就会沿着直线一直走下去，越走越远，无法被任何圆圈圈住。
        results = []
        
        # 方向向量：上(北), 右(东), 下(南), 左(西)
        # 顺时针方向：0: 北, 1: 东, 2: 南, 3: 西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for command in commands:
            x, y = 0, 0
            d = 0  # 初始朝北 (index 0)
            
            for c in command:
                if c == 'G':
                    dx, dy = directions[d]
                    x += dx
                    y += dy
                elif c == 'L':
                    d = (d - 1) % 4  # 向左转 90 度
                elif c == 'R':
                    d = (d + 1) % 4  # 向右转 90 度
            
            # 满足以下任意条件即被限制在圆内：
            # 1. 回到了原点 (x == 0 and y == 0)
            # 2. 最终朝向发生了改变 (d != 0) #🔥LGRG抵消的不算
            if (x == 0 and y == 0) or d != 0:
                results.append("YES")
            else:
                results.append("NO")
                
        return results