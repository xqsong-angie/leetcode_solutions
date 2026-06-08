#20250922
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
    

#20260607
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for c in s:
            if not stack or stack[-1]!=c:
                stack.append(c)
            else:
                stack.pop()
                
        return "".join(stack)