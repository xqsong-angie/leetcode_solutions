class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        cur_end = 0    # 当前这跳能到达的最远边界
        farthest = 0   # 下一跳能到达的最远位置

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:        # 走到边界了，必须跳一次
                count += 1
                cur_end = farthest
        
        return count