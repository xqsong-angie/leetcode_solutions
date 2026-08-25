#20260823
#不会
class Solution:
    def solution(self, words: list[str]) -> int:
        # 1. 按照字符串长度从小到大排序
        # 确保较短的单词先进入哈希表
        words.sort(key=len)#🔥从短到长的排法[a,a,b,ba,ca,cba]
        
        freq = {}
        ans = 0
        
        for word in words:
            # 找到当前 word 的所有后缀
            # 例如 "comeback" 的后缀有: "comeback", "omeback", ..., "ck", "k"
            # 顺便统计它与以前出现过的短单词（或同长等长单词）形成的配对数
            n = len(word)
            for i in range(n):
                suffix = word[i:]  # 提取后缀
                if suffix in freq:
                    ans += freq[suffix]
            
            # 将当前单词存入哈希表
            freq[word] = freq.get(word, 0) + 1
            
        return ans