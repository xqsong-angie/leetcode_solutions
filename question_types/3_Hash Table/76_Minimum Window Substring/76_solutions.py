#20260804
#错：
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt=Counter(t)
        s_cnt=defaultdict(int)
        s_idx=defaultdict(int)
        i=0
        min_len=len(s)
        res=""
        for j in range(len(s)):
            if s[j] in t_cnt:
                s_cnt[s[j]]+=1
                s_idx[s[j]]=j
            if s[i] not in t_cnt:
                i+=1 #🔥i指针移动方式有问题
            if s_cnt==t_cnt and j-i+1<=min_len:#update
                res=s[i:j+1]
                min_len=min(min_len,j-i+1)
                s_cnt=defaultdict(int) #🔥s_cnt不应该完全清空
                i=j
        return res
    
#对：🔥滑动窗口模板不清楚，
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 统计 t 中每个字符需要的数量
        t_cnt = Counter(t)
        # 记录当前窗口中字符的数量
        s_cnt = defaultdict(int)
        
        # t 中有多少种不同的字符
        need_types = len(t_cnt)
        # 当前窗口已经满足了多少种字符的数量要求
        valid_types = 0 
        
        i = 0
        min_len = float('inf') # 初始设置为无限大
        res = ""
        
        # j 是右指针，不断向右扩张窗口
        for j in range(len(s)):
            char = s[j]
            s_cnt[char] += 1
            
            # 如果当前字符是 t 中需要的，并且数量刚好满足了，满足的种类数 +1
            if char in t_cnt and s_cnt[char] == t_cnt[char]:
                valid_types += 1
            
            # 【核心逻辑】：只要当前窗口完全包含了 t（是一个合法窗口）🔥数量可以大于等于
            # 就开始尝试移动左指针 i，缩小窗口
            while valid_types == need_types:
                # 1. 更新最小窗口记录
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    res = s[i : j+1]
                
                # 2. 准备把左边的字符移出窗口
                left_char = s[i]
                
                # 如果移出的是 t 中需要的字符，并且移出后数量不够了，满足的种类数 -1
                if left_char in t_cnt and s_cnt[left_char] == t_cnt[left_char]:
                    valid_types -= 1
                
                # 在字典中扣除该字符，左指针前移 🔥对应字符数量减一
                s_cnt[left_char] -= 1
                i += 1
                
        return res