#20260811
#错：
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        s_list=s.split()#https://www.w3schools.com/python/ref_string_split.asp🔥会把数字逐位拆散
        i=0
        while i<len(s):
            if s[i].isdigit():#https://www.w3schools.com/python/ref_string_isdigit.asp
                stack.append(s[i])
                i+=1
            elif s[i]=="*":
                top1=stack.pop()
                top2=s[i+1]
                stack.append(top1*top2)
                i+=2
            elif s[i]=="/":
                top1=stack.pop()
                top2=s[i+1]
                if top1/top2>=0:
                    stack.append(top1//top2)
                else:
                    stack.append(ceil(top1/top2))
            elif s[i]=="-":
                stack.append(s[i])
                i+=1
        flag=True
        for i in range(len[stack]):
            sum=0#🔥每次循环会重置sum
            if stack[i]=="-":
                flag=False
            else:
                if flag==False:
                    sum-=int(stack[i])
                    flag=True
                else:
                    sum+=int(stack[i])
        return sum

#对：
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0       # 记录当前拼接出的数字
        sign = '+'    # 记录当前数字前面的符号，默认第一个数是正数
        
        for i in range(len(s)):
            char = s[i]
            
            # 如果是数字，累加拼接出多位数 (比如 '4'和'2' 拼成 42)
            if char.isdigit():
                num = num * 10 + int(char)
                
            # 如果遇到了操作符，或者已经到了字符串的最后一位
            # (注意不能用 elif，因为到了最后一位时既要拼接数字，也要处理进栈逻辑)
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':#🔥注意这里用sign判断，不是char,sign记录的是上一个符号
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)  # 减号直接存入负数，最后统一求和
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # Python 中的 // 是向下取整 (-3//2 = -2)
                    # 但题目要求向零取整 (-3/2 向零取整是 -1)
                    # int() 直接截断小数部分，完美符合向零取整的要求
                    stack.append(int(stack.pop() / num))
                
                # 处理完当前数字后，更新 sign 为新的符号，并把 num 清零，准备迎接下一个数字
                sign = char
                num = 0
                
        # 栈里面现在全是带着正负号的数字，直接求和即可
        return sum(stack)


