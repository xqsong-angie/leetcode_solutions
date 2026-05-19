#https://algo.monster/liteproblems/42
class Solution:

    def trap(self, height: List[int]) -> int:
        n=len(height)
        m_stack=[]
        sum=0
        for i in range(n):
            if not m_stack:
                m_stack.append(i)
            else:
                if height[i]<=height[m_stack[-1]]:
                    m_stack.append(i)
                else:
                    top=m_stack.pop()
                    if m_stack:
                        sum+=(i-m_stack[-1]-1)*(min(height[i],height[m_stack[-1]])-height[top])
                        while  m_stack and height[i]>height[m_stack[-1]]:
                            top=m_stack.pop()
                            if m_stack:
                                sum+=(i-m_stack[-1]-1)*(min(height[i],height[m_stack[-1]])-height[top])
                    m_stack.append(i)
     

        return sum
            
