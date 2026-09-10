#我的思路：遍历每条路径，然后看看每条路径和最大路径差多少，累加起来，可是这样会计算重复 

class Solution:
    def solution(self,n,m,latency):
        path_latency=[]
        def path(sum,i,m,latency):
            if i>m:#not root
                return 
            elif 2*i+1>m: #leaf
                return sum
            else:#not leaf node
                if 2*i+1<=m:
                    return latency[2*i]+path(2*i+1,m,latency)
                if 2*i+1<=m:
                    return latency[2*i+1]+path(2*i+2,m,latency)

        path(0,0,m,latency) 

#树形dp：尽可能在靠近根节点的边上加延迟
class Solution:
    def minAdditionalLatency(self, n: int, latency: list[int]) -> int:
        # dp[i] 表示从节点 i 到其子树内所有叶子节点的最大路径延迟
        dp = [0] * n
        total_increments = 0

        # 从最后一个非叶子节点开始，自底向上遍历到根节点 (0)
        # 最后一个非叶子节点的索引为 (n - 2) // 2
        last_non_leaf = (n - 2) // 2

        for i in range(last_non_leaf, -1, -1):
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            # 注意：边 latency[k] 对应的节点关系
            # 连接 i 和 2i+1 的边是 latency[2i]
            # 连接 i 和 2i+2 的边是 latency[2i+1]
            left_path = latency[2 * i] + dp[left_child]
            right_path = latency[2 * i + 1] + dp[right_child]

            # 累加左右两条子路径对齐所需的最小差值
            total_increments += abs(left_path - right_path)

            # 更新当前节点 i 向上传递的最大路径长度
            dp[i] = max(left_path, right_path)

        return total_increments