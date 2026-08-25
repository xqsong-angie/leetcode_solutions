#20260823
#不会
from collections import defaultdict
class Solution:
    def solution(self, numbers: list[int]) -> int:
        mask_counts = defaultdict(int)   # 统计每个掩码出现的次数
        exact_counts = defaultdict(int)  # 统计完全相同的原数字出现的次数

        ans = 0
        
        for num in numbers:
            s = str(num)
            L = len(s)
            
            # 1. 遍历当前数字能生成的所有掩码
            for i in range(L):#i是放*的位置
                mask = s[:i] + "*" + s[i+1:]  #🔥生成变体：每一位轮流用通配符代替，遍历一次是n
                
                # 如果之前有数字生成过相同的 mask，说明它们只差这 1 位
                ans += mask_counts[mask]#🔥原来mask_counts[mask]的数量代表有多少对
                
                # 记录该 mask 出现次数
                mask_counts[mask] += 1#🔥往后就把当前的算进去了
                
            # 2. 扣除完全相同的数字带来的误判🔥完全相同的数也会有一样的mask
            # 🔥因为完全相同的数字会在 L 个 mask 上全部重合
            if s in exact_counts:#🔥说明这个数字出现过了
                ans -= exact_counts[s] * L#🔥这个数字一共出现过的次数*mask匹配到的次数
                
            # 记录当前原数字出现的次数
            exact_counts[s] += 1
            
        return ans