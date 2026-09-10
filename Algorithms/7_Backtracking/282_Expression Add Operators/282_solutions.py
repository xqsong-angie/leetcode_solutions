#20260703
#https://www.youtube.com/watch?v=tunRDBsP7OQ
#错：
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        n=len(num)
        def backtracking(pt:int,cur_sum:int,prev:int,res:list,path:str,n:int):
            if pt>=n:
                if cur_sum==target:
                    res.append(path)
            else:
                if num[pt]==0:
                    return
                else:
                    for i in range(pt+1,n+1):
                        cur=int(num[pt:i])
                        #+
                        backtracking(i,cur_sum+cur,cur,res,path+"+"+str(cur),n) #“+1+2+3”
                        #-
                        backtracking(i,cur_sum-cur,-cur,res,path+"-"+str(cur),n)
                        #*
                        backtracking(i,cur_sum-prev+prev*cur,prev*cur,res,path+"*"+str(prev*cur),n)#path+"*"+str(prev*cur)字符串要拼入当前数
        backtracking(0,0,0,res,"",n)
        
        return res
#对：
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        n=len(num)
        def backtracking(pt:int,cur_sum:int,prev:int,path:str):
            if pt>=n:
                if cur_sum==target:
                    res.append(path)
            else:
                if num[pt]==0:
                    return
                else:
                    for i in range(pt+1,n+1):
                        cur_str=num[pt:i]
                        if len(cur_str) > 1 and cur_str[0] == '0': #排除先导0问题，e,g.,"05"
                            break
                        cur=int(cur_str)
                        if pt == 0: #第一个数字不需要加符号
                            backtracking(i, cur, cur, cur_str)
                        else:
                            #+
                            backtracking(i,cur_sum+cur,cur,path+"+"+cur_str)
                            #-
                            backtracking(i,cur_sum-cur,-cur,path+"-"+cur_str)
                            #*
                            backtracking(i,cur_sum-prev+prev*cur,prev*cur,path+"*"+cur_str) 
        
        backtracking(0,0,0,"")
        return res

#20260712 看了一遍，还是不能自己完全看懂，上面的代码有错误其实，以下为正确版本
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        n=len(num)
        def backtracking(pt:int,cur_sum:int,prev:int,path:str):
            if pt==n:
                if cur_sum==target:
                    res.append(path)
            else:#pt<n
                for i in range(pt+1,n+1):
                    cur_str=num[pt:i]#第一个数
                    if len(cur_str) > 1 and cur_str[0] == '0': #排除先导0问题，e,g.,"05"，但如果是“0”，可以跑通
                        break
                    cur=int(cur_str)#转化成整数
                    if pt == 0: #第一个数字不需要加符号
                        backtracking(i, cur, cur, cur_str)
                    else:
                        #+
                        backtracking(i,cur_sum+cur,cur,path+"+"+cur_str)
                        #-
                        backtracking(i,cur_sum-cur,-cur,path+"-"+cur_str)
                        #*
                        backtracking(i,cur_sum-prev+prev*cur,prev*cur,path+"*"+cur_str) #遇到乘法，相当于要把前一个数pop出来，乘完了再压栈
        backtracking(0,0,0,"")
        return res