class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        m_stack=[]
        
        for i in range(n):
            if not m_stack:
                m_stack.append(i)
            else:
                if temperatures[i]<=temperatures[m_stack[-1]] or not m_stack:
                    m_stack.append(i)
                else:
                    result[m_stack[-1]]=i-m_stack[-1]
                    m_stack.pop()
                    while m_stack and temperatures[i]>temperatures[m_stack[-1]]:
                        result[m_stack[-1]]=i-m_stack[-1]
                        m_stack.pop()
                    m_stack.append(i)

        return result

        