class Solution:
    def isnum(self, s: str) -> bool:
        try:
            float(s)  
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        mystack=[]
        for i in range(n):
            if self.isnum(tokens[i]):
                mystack.append(tokens[i])
            else:
                top2=int(mystack.pop())
                top1=int(mystack.pop())
                if tokens[i]=="+":
                    mystack.append(top1+top2)
                elif tokens[i]=="-":
                    mystack.append(top1-top2)
                elif tokens[i]=="*":
                    mystack.append(top1*top2)
                elif tokens[i]=="/":
                    mystack.append(top1/top2)
        return int(mystack[-1])