#20260802
#错：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>1:
            max_len=1
            i=0
            j=1
            hash_dict={s[i]:i} #store first idx
            while i<=j and j<len(s):
                if s[j] in hash_dict:
                    i=hash_dict[s[j]]+1
                    hash_dict.pop(s[j])#🔥这里会导致i指针回退，i指针是不能回退的
                    #remove an item from dict: https://www.w3schools.com/python/python_dictionaries_remove.asp
                max_len=max(max_len,j-i+1)
                hash_dict[s[j]]=j
                j+=1
            return max_len

        else:
            return len(s)
            
#对：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}  # 记录字符最后一次出现的索引
        max_len = 0
        i = 0  # 窗口左边界
        
        for j in range(len(s)):  # j 是窗口右边界
            # 如果字符出现过，且它最后一次出现的位置在当前窗口内 (>= i)
            if s[j] in hash_dict and hash_dict[s[j]] >= i:#🔥在窗口之外的不要管
                # 将左边界移动到该字符上次出现位置的下一位
                i = hash_dict[s[j]] + 1
                
            # 更新/添加该字符的最新索引
            hash_dict[s[j]] = j
            
            # 计算当前窗口长度并更新最大值
            max_len = max(max_len, j - i + 1)
            
        return max_len