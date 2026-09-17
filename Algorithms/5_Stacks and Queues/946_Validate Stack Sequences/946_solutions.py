#20260916
#错
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        len_pushed=len(pushed)
        len_popped=len(popped)
        if len_popped!=len_pushed:
            return False
        else:
            stack=[]
            push_pt=0
            pop_pt=0
            while pop_pt<len_popped:
                if not stack:
                    for i in range(push_pt,len_pushed):
                        if pushed[i]!=popped[pop_pt]:
                            stack.append(pushed[i])
                        else:
                            break
                    push_pt=i+1
                    pop_pt+=1
                else:#🔥这道题我在pushed的条件上卡住了，就是pop的下一个，有可能在还没push的那一段，也有可能在已经push的那一段，这两段如何分别写条件，多一个visited吗 


                    while stack[-1]!=popped[pop_pt]:
                        stack.pop()
                        pop_pt+=1
                    return False
            return True
        
#对
class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_pt = 0
        
        for x in pushed:
            stack.append(x)  # 依次将元素压入栈
            # 只要栈顶元素等于当前需要弹出的元素，就持续弹出，如果不是，就说明
            while stack and stack[-1] == popped[pop_pt]:
                stack.pop()
                pop_pt += 1
                
        # 如果所有元素都成功匹配并弹出，栈最终应该为空
        return len(stack) == 0