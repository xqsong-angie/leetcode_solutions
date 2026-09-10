class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0  # 走完一圈之后，油箱里剩余的净油量（无论从哪个位置开始，结果都是一样的）
        tank = 0        # 当前油量
        start = 0       # 候选起点

        for i in range(len(gas)):
            diff = gas[i] - cost[i]#离开当前位置能带走的油量
            total_tank += diff
            tank += diff
            if tank < 0:        # 从start到i走不通
                start = i + 1   # 直接跳过，从i+1重新尝试
                tank = 0

        return start if total_tank >= 0 else -1

#20260712 看了一遍，对total_tank有点没理解

