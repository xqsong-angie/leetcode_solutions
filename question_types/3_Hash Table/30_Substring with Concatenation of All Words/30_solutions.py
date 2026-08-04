#20260804
#错：还是滑动窗口问题
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res=[]
        i=0
        seen=set()
        word_cnt=Counter(words)
        word_temp=word_cnt #🔥可变结构的存档要用copy
        k=len(words[0])
        for j in range(0,len(s)-k+1,k): #🔥漏掉了起点非整数倍的情况
            temp=s[j:j+k]
            if temp in word_cnt and word_cnt[temp]>0:
                seen.add(temp)
                word_cnt[temp]-=1
            else:
                if seen==set(words):
                    res.append(i)
                i=j+k
                word_cnt=word_temp
                seen=set()
        return res
    
#对：
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        k = len(words[0])
        word_num = len(words)
        res = []
        
        # 目标单词频次字典
        target_cnt = Counter(words)
        
        # 只需要遍历 k 种不同的起点偏移量
        for offset in range(k):
            # 每个偏移量下，维护一个独立的滑动窗口
            left = offset
            right = offset
            window_cnt = Counter()
            match_words = 0  # 记录当前窗口内有效匹配的单词数
            
            # 右指针以 k 为步长向右扩张
            while right + k <= len(s):
                # 截取右边的一个单词
                word = s[right : right+k]
                right += k # 右指针移动
                
                if word in target_cnt:
                    window_cnt[word] += 1
                    match_words += 1
                    
                    # 遇到多余的合法单词，左指针开始收缩！
                    # 比如需要1个"foo"，现在窗口里有2个"foo"，左边就要吐出单词
                    while window_cnt[word] > target_cnt[word]:
                        left_word = s[left : left+k]
                        window_cnt[left_word] -= 1
                        match_words -= 1
                        left += k # 左指针以 k 为步长收缩
                    
                    # 如果匹配的单词数量正好等于所需的总单词数，说明找到了一个合法解
                    if match_words == word_num:
                        res.append(left)
                
                else:
                    # 如果遇到完全不在 words 里的单词，前面的积累全部作废
                    # 清空窗口状态，左指针直接跳到当前右指针的位置
                    window_cnt.clear()
                    match_words = 0
                    left = right
                    
        return res