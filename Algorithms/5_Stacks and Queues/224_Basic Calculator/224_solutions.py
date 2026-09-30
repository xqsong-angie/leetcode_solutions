#20260929
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        while i<n:
            if s[i]=="(":
                stack.append()
            if s[i]==")":
                res=0
                top1=stack.pop()
                top2=stack.pop()
                if top1.isdigit():
                    pass
                    #感觉条件越写越乱，好像没有一个固定的顺序处理-和+

#答案：
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0      # 当前层累加的结果
        num = 0      # 当前正在解析的数字
        sign = 1     # 1 表示 positive (+), -1 表示 negative (-)
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]

            if ch.isdigit():
                num = 0
                # 连续读取完整的数字（如 "123"）
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # 读完数字后直接应用符号并累加到 res
                res += sign * num
                continue  # 因为 i 已经指向下一个字符，跳过末尾的 i += 1

            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                # 1. 把括号前的 res 和 sign 压栈保存
                stack.append(res)
                stack.append(sign)
                # 2. 重置 res 和 sign，准备计算括号内部
                res = 0
                sign = 1
            elif ch == ')':
                # 1. 先乘上括号外的符号
                res *= stack.pop()  # 弹出的是 sign
                # 2. 再加上括号前的累加值
                res += stack.pop()  # 弹出的是之前的 res

            i += 1

        return res