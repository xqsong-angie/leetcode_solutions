#20260929
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[]#🔥栈里存的应该是“每一层括号对应的原子计数字典 (Counter/HashMap)”，而不是单个字符
        i=0
        n=len(formula)
        cnt=defaultdict(int)
        while i<n:#https://www.w3schools.com/python/ref_string_isupper.asp
            if formula[i].isupper():
                ele=formula[i]
                i+=1
                if i==n:
                    break
                while i<n and formula[i].islower():
                    ele+=formula[i]
                    i+=1
                stack.append(ele)
                if formula[i].isdigit():#🔥如果数字是两位数处理不了
                    top=stack.pop()
                    if top.isalpha():
                        cnt[top]+=int(formula[i])
                    i+=1
            elif formula[i]=="(" or formula[i]==")":
                stack.append(formula[i])
                i+=1
            elif formula[i].isdigit():
                if stack:
                    top=stack.pop()
                    if top.isalpha():
                        cnt[top]+=int(formula[i])
                    elif top==")":#🔥当遇到右括号 ) 后的数字（比如 (SO3)2 后的 2）时，括号里面的每个元素数量都要乘以这个数字
                        while stack[-1]!="(":
                            top=stack.pop()
                            cnt[top]+=int(formula[i])
                        stack.pop()
                        i+=1
        while stack:
            top=stack.pop()
            cnt[top]+=1
        res=""
        sorted_dict = dict(sorted(cnt.items(), key=lambda item: item[0]))
        for k,v in sorted_dict.items():
            if v==1:
                res+=k
            else:
                res+=k+str(v)
        return res
    
#答案
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [defaultdict(int)]  # 栈底是全局/最外层的计数字典
        i = 0
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))#🔥压入一个新的dict用来代表内层括号的cnt
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                # 读取括号后面的完整数字
                while i < n and formula[i].isdigit():#🔥用while读取所有数位
                    i += 1
                mult = int(formula[start:i]) if start < i else 1
                
                # 弹出当前括号层的字典，乘以 mult 后合并到上一层
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * mult#🔥可以直接乘但不能直接合并
            else:
                # 解析元素名称（1个大写 + 若干小写）
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                
                # 解析元素后面的数字
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1
                
                # 加到当前层字典中
                stack[-1][atom] += count
        
        # 将最外层字典按字典序排序输出
        final_cnt = stack[-1]
        res = []
        for atom in sorted(final_cnt.keys()):
            res.append(atom)
            if final_cnt[atom] > 1:
                res.append(str(final_cnt[atom]))
                
        return "".join(res)