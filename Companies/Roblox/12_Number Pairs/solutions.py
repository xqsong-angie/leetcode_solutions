#20260823

class Solution:
    def solution(self,a,b):
        ans=0
        for j in range(len(b)):
            for i in range(j+1):#a
                if a[i] - b[j] == a[j] - b[i]:
                    ans+=1
        return ans


#优化
from collections import Counter

class Solution:
    def solution(self, a: list[int], b: list[int]) -> int:
        # 计算每个位置的 a[k] + b[k] 并统计频次
        counts = Counter(x + y for x, y in zip(a, b))#🔥把式子移项转化为a[i]+b[i]=a[j]+b[j]
        #令C[i]=a[i]+b[i],C[j]=a[j]+b[j],所以要算出逐位相加的结果，每一个x + y，都对应一个不同的下标。
        ans = 0
        # 对每个数值的出现频次 K，计算 C(K, 2) + K
        for k in counts.values():
            ans += k * (k + 1) // 2#C(K, 2)是i<j的情况，k是相等的情况
            
        return ans