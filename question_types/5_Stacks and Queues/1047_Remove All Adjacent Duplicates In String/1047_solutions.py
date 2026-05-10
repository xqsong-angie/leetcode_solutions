class Solution:
    def removeDuplicates(self, s: str) -> str:
        mystack=[]
        n=len(s)
        s=list(s)
        count=0
        for i in range(n):
            if not mystack:
                mystack.append(s[i])
            elif s[i]==mystack[-1]:
                mystack.pop()
                count+=2
            else:
                mystack.append(s[i])
        
        return "".join(mystack)
