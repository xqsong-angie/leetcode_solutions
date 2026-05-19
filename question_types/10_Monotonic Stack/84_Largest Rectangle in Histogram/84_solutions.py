class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        m_stack=[]
        heights=[0]+heights+[0]
        n=len(heights)
        
        for i in range(n):
            if not m_stack:
                m_stack.append(i)
            else:
                if heights[i]>=heights[m_stack[-1]]:
                    m_stack.append(i)
                else:
                    while m_stack and heights[i]<heights[m_stack[-1]]:
                        top=m_stack.pop()
                        if m_stack:
                            width=i-m_stack[-1]-1
                            height=heights[top]
                            max_area=max(max_area,width*height)
                    m_stack.append(i)  
        return max_area

                        
