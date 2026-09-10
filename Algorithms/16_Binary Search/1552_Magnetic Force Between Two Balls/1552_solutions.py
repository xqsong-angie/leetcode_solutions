#20260704
#错：
#https://www.w3schools.com/python/ref_func_abs.asp
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        diff=[position[i+1]-position[i] for i in range(len(position)-1)]
        low=min(diff) #如果每个桶都要放球
        high=sum(diff)#如果只有两个球
        #球的个数为x,force为y,单调递减
        while low<=high:
            mid=(low+high)//2
            ball_cnt=2
            cur_sum=0
            for i in range(len(diff)):
                if cur_sum+diff[i]<=mid:
                    cur_sum+=diff[i]
                else:#cur_sum+diff[i]>mid
                    ball_cnt+=1
                    cur_sum=diff[i]
            if ball_cnt>m: #mid太小 
                low=mid+1
            else:#ball_cnt<=m mid太大
                high=mid-1
        return low
#对：
"""minimum magnetic force between any two balls is maximum.
具体一种摆放方式的最小距离，要是该数量球的所有摆放方式的最大"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        diff=[position[i+1]-position[i] for i in range(len(position)-1)]
        low=min(diff) #如果每个桶都要放球
        high=sum(diff)#如果只有两个球
        #球的个数为x,force为y,单调递减
        while low<=high:
            mid=(low+high)//2
            ball_cnt=1 #🔥开头只放了一个球，不要再多放一个
            cur_sum=0
            for i in range(len(diff)):
                if cur_sum+diff[i]<mid:
                    cur_sum+=diff[i]
                else:#cur_sum+diff[i]>=mid
                    ball_cnt+=1
                    cur_sum=0
            if ball_cnt>=m: #mid太小 🔥(ball_cnt==m时，说明mid合理，因为找最大值，所以要把mid上推)
                low=mid+1
            else:#ball_cnt<m mid太大
                high=mid-1
        return high