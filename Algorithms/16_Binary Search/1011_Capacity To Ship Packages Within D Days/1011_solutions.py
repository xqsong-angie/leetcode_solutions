#20260704
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        n=len(weights)
        while low<=high:#x轴为天数，y轴为cap, 单调递减
            mid=(low+high)//2
            cur_sum=0
            count=1
            for i in range(n):
                if cur_sum+weights[i]<=mid:
                    cur_sum+=weights[i]
                else:
                    count+=1
                    cur_sum=weights[i]
            if count>days: #说明mid太小了，要变大,区间右移
                low=mid+1
            else:#count<=days, <和=都有mid过大的嫌疑，要变小，区间左移
                high=mid-1
        return low