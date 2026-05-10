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