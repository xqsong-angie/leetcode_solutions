#20260727 前缀和+哈希表，看到“连续子数组求和/计数”就往这里想
#错：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表映射：前缀和 -> 该前缀和出现的索引列表
        # 初始化 prefix_sum = 0 在索引 -1 处
        prefix_map = set()#🔥不能只记录某个前缀和有没有出现过，以为可能有同一个end不同start的情况，要加两次
        curr_sum = 0
        result = 0
        for num in nums:
            curr_sum += num
            if curr_sum-k in prefix_map:
                result+=1  
            prefix_map.add(curr_sum)
        if k in prefix_map:
            result+=1
        return result
    
#对：
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表保存：前缀和 -> 出现的次数
        # 初始化 prefix_map[0] = 1，代表前缀和为 0 默认出现过 1 次（处理从 index 0 开始的子数组）
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        curr_sum = 0
        result = 0
        
        for num in nums:
            curr_sum += num
            # 如果 (curr_sum - k) 之前出现过，把出现的次数累加到 result 中
            if (curr_sum - k) in prefix_map:
                result += prefix_map[curr_sum - k]
            # 更新当前前缀和的出现次数
            prefix_map[curr_sum] += 1
            
        return result