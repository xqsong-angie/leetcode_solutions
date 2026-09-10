#20260620
#错：
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            if s[i]=="]":
                part=[]
                while stack[-1]!="[":
                    part.append(stack.pop())
                stack.pop() #pop "["
                k=stack.pop() #get k (这个方法无法应对多位数)
                part.reverse()
                for _ in range(int(k)):
                    stack.extend(part) #put substring back(https://www.w3schools.com/python/ref_list_reverse.asp)
            else:
                stack.append(s[i])
        return "".join(stack)
#对：
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        n=len(s)
        for i in range(n):
            if s[i]=="]":
                part=[]
                while stack[-1]!="[":
                    part.append(stack.pop())
                stack.pop() #pop "["
                k="" #!!!这里加循环，注意也要reverse
                while stack and not stack[-1].isalpha() and stack[-1]!="[":
                    k+=stack.pop() #get k
                part.reverse()
                for _ in range(int(k[::-1])):#reverse str: https://www.w3schools.com/python/python_howto_reverse_string.asp
                    stack.extend(part) #put substring back(https://www.w3schools.com/python/ref_list_reverse.asp)
            else:
                stack.append(s[i])
        return "".join(stack)
    
#20260811
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isdigit() or s[i]=="[" or s[i].isalpha():
                stack.append(s[i])
            else:
                letters=""
                digits=""
                cnt=0
                while stack:
                    if stack[-1].isalpha() and cnt==0:
                        letters+=stack.pop()
                    elif stack[-1]=="[" and cnt==0:
                        stack.pop()
                        cnt+=1
                    elif s[i].isdigit():#🔥这里把stack[-1]错写成s[i]了，导致invalid literal for int() with base 10
                        digits+=stack.pop()
                    else:
                        break
                res=int(digits[::-1])*letters[::-1]
                #https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
                for r in res:
                    stack.append(r)
        return "".join(stack)
                
#对：
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isdigit() or s[i]=="[" or s[i].isalpha():
                stack.append(s[i])
            else:
                letters=""
                digits=""
                cnt=0
                while stack:
                    if stack[-1].isalpha() and cnt==0:
                        letters+=stack.pop()
                    elif stack[-1]=="[" and cnt==0:
                        stack.pop()
                        cnt+=1
                    elif stack[-1].isdigit():
                        digits+=stack.pop()
                    else:
                        break
                res=int(digits[::-1])*letters[::-1]
                #https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
                for r in res:
                    stack.append(r)
        return "".join(stack)
                