class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
        for c in s:
            if c=='(' or c=='{' or c=='[':
                mystack.append(c)
            else:
                if not mystack:
                    return False
                elif c==")" and mystack[-1]=="(":
                    mystack.pop()
                elif c=="}" and mystack[-1]=="{":
                    mystack.pop()
                elif c=="]" and mystack[-1]=="[":
                    mystack.pop()
                else:
                    return False
        if not mystack:
            return True
        else:
            return False

#20260606
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if c==")":
                        if stack[-1]=="(":
                            stack.pop()
                        else:
                            return False
                    elif c=="]":
                        if stack[-1]=="[":
                            stack.pop()
                        else:
                            return False
                    else:
                        if stack[-1]=="{":
                            stack.pop()
                        else:
                            return False

        return False if stack else True
        