#20250920
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        i=0
        s=list(s)
        res=""
        while i*2*k<n-1:
            left=i*2*k
            right=min(n-1,i*2*k+k-1)
            while left<right:
                temp=s[left]
                s[left]=s[right]
                s[right]=temp
                left+=1
                right-=1
            i+=1
        for c in s:
            res+=c
        return res
    

#20260606
class Solution:
    #https://www.w3schools.com/python/ref_list_reverse.asp
    def reverseStr(self, s: str, k: int) -> str:
        s_list=list(s)
        n=len(s_list)
        res=[]
        for i in range(n):
            if i%(2*k)==0:
                sub=s_list[i:i+k]
                sub.reverse() 
                res+=sub
                res+=s_list[i+k:i+2*k]
        return ('').join(res)
