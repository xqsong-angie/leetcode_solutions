class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:#和接雨水那道题刚好反过来
        max_area=0
        m_stack=[]
        heights=[0]+heights+[0]#左右设置一个面积为0的方块
        n=len(heights)
        
        for i in range(n):
            if not m_stack:
                m_stack.append(i)
            else:
                if heights[i]>=heights[m_stack[-1]]:#反过来了，这次是递减栈，栈口最大，栈底最小
                    m_stack.append(i)
                else:
                    while m_stack and heights[i]<heights[m_stack[-1]]:
                        top=m_stack.pop()#凸起（高柱） 来向两边延伸
                        if m_stack:
                            width=i-m_stack[-1]-1#索引差
                            height=heights[top]#一个凸起
                            max_area=max(max_area,width*height)
                    m_stack.append(i)  
        return max_area

#20260723 看了一遍 有点难
