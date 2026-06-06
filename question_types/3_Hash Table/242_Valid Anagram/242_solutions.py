class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #letter frequency->list
       #hash: set, list,dict
       freq=[0]*26
       offset=ord("a")
       for letter in s:
            freq[ord(letter)-offset]+=1
       for letter in t:
            freq[ord(letter)-offset]-=1
       for i in range(len(freq)):
            if freq[i]!=0:
                return False
       return True
        
#20260605
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count=Counter(s)
        t_count=Counter(t)
        if s_count==t_count:
            return True
        else:
            return False
