#错：
from collections import defaultdict
class Solution:
    def betterCompression(self,S):
        cnt=defaultdict(int)
        S_compressed=""
        freq="0"
        cur_letter=""
        for i in range(len(S)):
            if S[i].isdigit():
                freq+=S[i]
            else:
                if i==0:
                    cur_letter=S[i]
                else:
                    cnt[cur_letter]+=int(freq)
                    cur_letter=S[i]
                    freq="0"
        cnt[cur_letter]+=int(freq)

        for k,v in cnt.items():#🔥k要升序排列
            S_compressed+=(k+v)#🔥v是int, 要按字符串输出
        return S_compressed

#对：
from collections import defaultdict
class Solution:
    def betterCompression(self,S):
        cnt=defaultdict(int)
        S_compressed=""
        freq="0"
        cur_letter=""
        for i in range(len(S)):
            if S[i].isdigit():
                freq+=S[i]
            else:
                if i==0:
                    cur_letter=S[i]
                else:
                    cnt[cur_letter]+=int(freq)
                    cur_letter=S[i]
                    freq="0"
        cnt[cur_letter]+=int(freq)

        for k in sorted(cnt.keys()):#🔥cnt.keys()是可迭代结构，可以排序
            S_compressed += k + str(cnt[k])
        return S_compressed