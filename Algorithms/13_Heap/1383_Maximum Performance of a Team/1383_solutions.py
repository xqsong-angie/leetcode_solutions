#20260930
class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        group=[g for g in zip(efficiency,speed)]
        group.sort(key=lambda x: x[0])
        for i in range(n):
            pass
            #是单调栈吗，有点像rectangle，但是这个不是连续的
        
#答案
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Zip and sort engineers by efficiency in DESCENDING order
        engineers = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)
        
        speed_heap = []
        speed_sum = 0
        max_perf = 0
        
        for eff, spd in engineers:
            # Add current engineer's speed to our team
            heapq.heappush(speed_heap, spd)
            speed_sum += spd
            
            # If team exceeds k members, remove the engineer with the smallest speed
            if len(speed_heap) > k:
                speed_sum -= heapq.heappop(speed_heap)#🔥弹出的engineer eff>=当前塞进来这个的eff(非常巧妙，保证了现在这个eff就是剩下k个里面最小的eff)
            
            # Calculate maximum performance with current efficiency as the minimum
            max_perf = max(max_perf, speed_sum * eff)
            
        return max_perf % MOD