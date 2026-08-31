class Solution:
    def encryptionValidity(self,instructionCount:int,validityPeriod:int,keys:list)->list:
        n=len(keys)
        d=[0]*n
        for i in range(n):
            for j in range(n):
                if keys[i]%keys[j]==0:#🔥忽略了Any divisor of a key must be greater than 1
                    d[i]+=1
        strength=max(d) * 10**5
        return [1,strength] if instructionCount*validityPeriod>=strength else [0,strength]
    
#对：
class Solution:
    def encryptionValidity(self,instructionCount:int,validityPeriod:int,keys:list)->list:
        n=len(keys)
        d=[0]*n
        for i in range(n):
            for j in range(n):
                if keys[j]>1 and keys[i]%keys[j]==0:#🔥如果一个 key 是 1，它的 d 值是 0
                    d[i]+=1
        strength=max(d) * 10**5
        return [1,strength] if instructionCount*validityPeriod>=strength else [0,strength]