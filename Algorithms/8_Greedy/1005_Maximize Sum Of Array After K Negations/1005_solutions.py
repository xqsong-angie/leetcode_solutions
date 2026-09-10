class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        flag=True
        while flag==True and k>0:#直到没有负数跳出循环，多出来的k当作全员正数处理走最后的分支
            flag=False#还原
            idx=-1
            largest_neg=0
            for i in range(len(nums)):#用于获取最大负数及其index
                if nums[i]<0:#如果本来就是负的
                    flag=True#说明找到一个负数
                    if largest_neg==0:
                        largest_neg=-nums[i]#最大负数（绝对值最大），优先转换最大负数为最大正数
                        idx=i#最大负数的index
                    else:
                        if largest_neg<-nums[i]:
                            largest_neg=-nums[i]
                            idx=i

            if idx>=0:#说明找到最大负数，如果全员正数，不走该分支
                nums[idx]=-nums[idx]
                k-=1

        if k>0:#还剩一些次数
            nums.sort()
            if k%2==0: #even
                return sum(nums)#直接返回
            else:#odd
                return sum(nums)-2*nums[0]#把最小的那个变负
        elif k==0:#此时结束处理
            return sum(nums)

#20260712 看了一遍