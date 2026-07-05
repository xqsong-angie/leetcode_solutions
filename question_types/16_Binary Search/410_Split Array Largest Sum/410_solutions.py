#20260628
#错：
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #https://www.bilibili.com/video/BV1rb411T7dR/?spm_id_from=333.337.search-card.all.click&vd_source=9902916331bef4c93586d2ad5780e0b0
        #二分答案题，最主要的是找到连续集
        #连续集含义：如果份数大于k份，说明和X选小了，如果份数小于k份，说明X选大了,所以是关于X的集[X1,X2,...,Xn]
        #！！！二分答案单调递减：最大和为x,份数为y；y随x单调递减
        low=max(nums)#分len(nums)份
        high=sum(nums)#分1份
        n=len(nums)
        #check 在最大总和为mid时，分出份数为多少
        def check(nums,n,mid):#🔥主要问题在这里
            cur_sum=0
            count=0#份数
            for i in range(n):
                if cur_sum<mid:
                    cur_sum+=nums[i]
                else:#🔥当前cur_sum大了，但是此时遍历到的nums[i]不见了
                    count+=1
                    cur_sum=0
            return count
        while low<=high:
            mid=(low+high)//2 #分k'份时得到最大总和为mid
            count=check(nums,n,mid)
            if count<=k: #count==k只能说明当前mid是合法的上限，但不一定是最小合法上限；同理count<k也是mid设置太大的情况，放在一起讨论
                high=mid-1
            else:#count>k不合法,>k的原因是mid设置太小了
                low=mid+1
        return low#return 什么取决于想要什么答案，low为最小合法值，high为最大合法值

#对：
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #https://www.bilibili.com/video/BV1rb411T7dR/?spm_id_from=333.337.search-card.all.click&vd_source=9902916331bef4c93586d2ad5780e0b0
        #二分答案题，最主要的是找到连续集
        #连续集含义：如果份数大于k份，说明和X选小了，如果份数小于k份，说明X选大了,所以是关于X的集[X1,X2,...,Xn]
        #！！！二分答案单调递减：最大和为x,份数为y；y随x单调递减
        low=max(nums)#分len(nums)份
        high=sum(nums)#分1份
        n=len(nums)
        #check 在最大总和为mid时，分出份数为多少
        def check(nums,n,mid):
            cur_sum=0
            count=1#🔥份数：要默认有1份
            for i in range(n):
                if cur_sum + nums[i] > mid:
                    count += 1
                    cur_sum=nums[i]#🔥放不下的数要放在新一段的开头而不是丢弃
                else: #🔥加上之后没超再加
                    cur_sum+=nums[i]
            return count
        while low<=high:
            mid=(low+high)//2 #分k'份时得到最大总和为mid
            count=check(nums,n,mid)
            if count<=k: #count==k只能说明当前mid是合法的上限，但不一定是最小合法上限；同理count<k也是mid设置太大的情况，放在一起讨论
                high=mid-1
            else:#count>k不合法,>k的原因是mid设置太小了
                low=mid+1
        return low#return 什么取决于想要什么答案，low为最小合法值，high为最大合法值



            
            
            


        