# def solution(fatherPos,martinPos,velFather,steps):
#     father_cur=fatherPos
#     martin_cur=martinPos
#     diff=float('inf')
    
#     for i in range(1,steps+1):
#         father_cur+=velFather
#         martin_cur=
#         diff=father_cur-

def solution(father_pos, martin_pos, vel_father, steps):
    # 1. 产生爸爸踩过的所有坐标点集合（包含起点，共 steps + 1 个点）
    father_steps_set = set(father_pos + i * vel_father for i in range(steps + 1))
    
    # 爸爸终点坐标
    father_max_pos = father_pos + steps * vel_father
    
    max_f = 0
    best_v2 = 1
    
    # 2. 枚举 Martin 所有可能的速度 V2（从 1 到 V1）
    # 当 V2 = 1 时，Martin 会踩过途径的所有整数点，重合数目必定最多
    for v2 in range(1, vel_father + 1):
        f_count = 0
        curr_pos = martin_pos
        
        # 沿着步长 V2 模拟，直到超出爸爸跑到的最大终点
        while curr_pos <= father_max_pos:
            if curr_pos in father_steps_set:
                f_count += 1
            curr_pos += v2
        
        # 3. 更新最大重合数 F 和最佳速度 V2
        # 注意：重合数相同时，优先选择更大的 V2
        if f_count > max_f or (f_count == max_f and v2 > best_v2):
            max_f = f_count
            best_v2 = v2
            
    return f"{max_f} {best_v2}"

# 对应 Example 测试：
# father_pos = 3, martin_pos = 2, vel_father = 2, steps = 20
print(solution(3, 2, 2, 20))  # 输出: 21 1

"""
不能用二分查找，因为 $V_2$ 与重合数 $F$ 之间不具备单调性（Monotonicity）。二分查找的前提条件是：目标函数必须是单调递增或单调递减的（或者呈现单峰/单谷的函数）。但这道题中，速度 $V_2$ 与重合脚印数 $F$ 的关系是非单调的、剧烈波动的。
"""