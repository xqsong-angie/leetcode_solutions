def solution(rates, strategy, k):
    n = len(rates)
    
    # 1. 计算未修改策略时的基础收益
    base_profit = 0
    for r, s in zip(rates, strategy):
        base_profit += r * s  # s为-1时扣除，0时不变，1时增加
        
    half_k = k // 2
    
    # 辅助函数：计算位置 idx 被设为 target_op 时的收益增量
    def get_delta(idx, target_op):
        orig_op = strategy[idx]
        price = rates[idx]
        orig_contrib = price * orig_op
        target_contrib = price * target_op
        return target_contrib - orig_contrib

    # 2. 计算第一个窗口 [0, k-1] 的增量
    current_gain = 0
    # 前半段改为 0
    for i in range(0, half_k):
        current_gain += get_delta(i, 0)
    # 后半段改为 1
    for i in range(half_k, k):
        current_gain += get_delta(i, 1)
        
    max_gain = current_gain
    
    # 3. 滑动窗口更新增量
    for i in range(1, n - k + 1):
        # 移出窗口最左侧的元素 (原属于前半段改为0)
        current_gain -= get_delta(i - 1, 0)
        
        # 中间交界的元素 (从前半段改为0 变成 改为1)
        mid_idx = i + half_k - 1
        current_gain -= get_delta(mid_idx, 0)
        current_gain += get_delta(mid_idx, 1)
        
        # 新移入窗口最右侧的元素 (属于后半段改为1)
        right_idx = i + k - 1
        current_gain += get_delta(right_idx, 1)
        
        max_gain = max(max_gain, current_gain)
        
    return base_profit + max_gain