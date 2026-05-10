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
                    
        