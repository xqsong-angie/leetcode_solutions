class Solution:
    def jump(self, nums: List[int]) -> int:#这题比jump game多一个找最少次跳路径，jump game只是判断能不能跳到
        count = 0
        cur_end = 0    # 当前这跳能到达的最远边界
        farthest = 0   # 下一跳能到达的最远位置

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])#i + nums[i]是当前位置能跳到的最远地方，下一跳能到达的最远位置
            if i == cur_end:        # 走到边界了，必须跳一次
                count += 1
                cur_end = farthest#下一跳变成当前跳了
        
        return count
    
#20260712 看了一遍