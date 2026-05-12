class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0  # 全局油量，判断有无解
        tank = 0        # 当前油量
        start = 0       # 候选起点

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            tank += diff
            if tank < 0:        # 从start到i走不通
                start = i + 1   # 直接跳过，从i+1重新尝试
                tank = 0

        return start if total_tank >= 0 else -1