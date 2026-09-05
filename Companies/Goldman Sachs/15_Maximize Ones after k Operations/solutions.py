class Solution:
    def solution(self,s,k):
        idx=-1
        one_cnt=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                if idx==-1:
                    idx=i#获得最右侧1的位置
                    one_cnt+=1
                else:#统计1的个数
                    one_cnt+=1
        zero_cnt=0
        for i in range(idx-1,-1,-1):#统计最右侧1左侧一共有多少-=0
            if s[i]=="0":
                zero_cnt+=1
        if k>=zero_cnt:
            return zero_cnt+one_cnt
        else:
            return one_cnt+k
        