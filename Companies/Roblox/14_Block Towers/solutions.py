#20260825
#🔥注意这道题是直接在塔上加块，无需交换顺序
def solution(towers: list[int]) -> int:
    n = len(towers)

    # 1. 计算变成严格递增 (Increasing) 所需的最少步数🔥即让第一个塔尽可能矮
    # 找到首个塔的最小可能高度 h,后面就是h+1,h+2
    #🔥第i个塔的目标高度为h+i, h+i>=tower[i],即h+i-tower[i]
    h_inc = max(towers[i] - i for i in range(n))#0，1，2，3这样是最小的情况
    # 累加每个塔需要增加的方块数
    moves_inc = sum((h_inc + i) - towers[i] for i in range(n))#所以h_dec + i对应h+1,h+2,...

    # 2. 计算变成严格递减 (Decreasing) 所需的最少步数
    # 找到首个塔的最小可能高度 h，后面就是h-1,h-2
    h_dec = max(towers[i] + i for i in range(n)) #3，2，1，0是最小的情况
    # 累加每个塔需要增加的方块数🔥第i个塔的目标高度为h-i, h-i>=tower[i],即h-i-tower[i]
    moves_dec = sum((h_dec - i) - towers[i] for i in range(n))#所以h_dec - i对应h-1,h-2,...

    # 返回两者的较小值
    return min(moves_inc, moves_dec)