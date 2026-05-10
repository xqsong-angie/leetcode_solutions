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
        
    
