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
    
#20260621
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for i in range(n):
            if tokens[i]=="/":
                num1=stack.pop()
                num2=stack.pop()
                stack.append(int(num2)/int(num1)) #"//" vs "/"
            elif tokens[i]=="+":
                num1=stack.pop()
                num2=stack.pop()
                stack.append(int(num2)+int(num1))
            elif tokens[i]=="*":
                num1=stack.pop()
                num2=stack.pop()
                stack.append(int(num2)*int(num1))
            elif tokens[i]=="-": #不要忘了这里，分单独的"-"和“-11”这种连着数字的
                num1=stack.pop()
                num2=stack.pop()
                stack.append(int(num2)-int(num1))
            else:
                stack.append(tokens[i])
        return int(stack[-1])