class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        m_stack=[]
        
        for i in range(n):
            if not m_stack:
                m_stack.append(i)#放索引，不放值
            else:
                if temperatures[i]<=temperatures[m_stack[-1]] or not m_stack:#递增栈，栈口的最小，栈底的最大
                    m_stack.append(i)
                else:
                    result[m_stack[-1]]=i-m_stack[-1]
                    m_stack.pop()#pop出m_stack[-1]，因为它已经计算完结果了
                    while m_stack and temperatures[i]>temperatures[m_stack[-1]]:#也有一种可能，就是栈里还有比当前小的，不过随着弹出越来越大，会在某个地方break
                        result[m_stack[-1]]=i-m_stack[-1]#计算每一个index
                        m_stack.pop()#计算完弹出
                    m_stack.append(i)#全部计算完，这个就是当前最小的，入栈

        return result
    
#20260723 看了一遍

        