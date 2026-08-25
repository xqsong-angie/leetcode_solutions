#20260823
#错：
class Solution:
    def solution(self,memory,queries):
        n=len(memory)
        id_counter=[0]*n
        res=[]
        for cmd,para in queries:
            if cmd==0:#alloc
                flag=False
                for i in range(0,n-7,8):#🔥界限有问题，最后一部分可能不到8
                    if set(memory[i:i+para])==0:#🔥set 和 int不能比较，且memory[i:i+para]如果后面长度不够para不会报错
                        flag=True
                        res.append(i)
                        for j in range(para):
                            memory[i+j]=1
                            id_counter+=1#🔥分完了要break,否则同一个cmd会被多次分配内存
                if flag==False:
                    res.append(-1)
            else:#erase
                flag=False
                length=0
                for id in id_counter:
                    if id==para:
                        flag=True
                    else:
                        if flag==True:
                            res.append(length)
                if flag==False:
                    res.append(-1)
        return res

#对：
class Solution:
    def solution(self,memory,queries):
        n=len(memory)
        id_counter=[0]*n
        res=[]
        id=0
        for cmd,para in queries:
            if cmd==0:#alloc
                flag=False
                for i in range(0, n - para + 1, 8):
                    if len(memory[i:i+para])==para and set(memory[i:i+para]) == {0}:
                        flag=True
                        res.append(i)
                        id+=1
                        for j in range(para):
                            memory[i+j]=1
                            id_counter[i+j]=id
                        break
                if flag==False:
                    res.append(-1)
            else:#erase
                length=0
                for i in range(n):
                    if id_counter[i]==para:
                        memory[i]=0
                        length+=1
                        id_counter[i]=0 #🔥清空后id也要删掉
                if length>0:
                    res.append(length)
                else:
                    res.append(-1)
        return res