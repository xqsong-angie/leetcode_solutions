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
                if height[i]<=height[m_stack[-1]]:#递增栈
                    m_stack.append(i)#这里都是凹下去的
                else:
                    top=m_stack.pop()#top（刚刚弹出的栈顶）： 代表凹槽的底部（池底）
                    if m_stack:
                        sum+=(i-m_stack[-1]-1)*(min(height[i],height[m_stack[-1]])-height[top])#“按行（横向）”一层一层地计算雨水体积
                        #i-m_stack[-1]-1：因为要减掉两侧只留中间，所以多-1
                        #min:中间能接多少水，取决于左右两个更短的那一个
                        #m_stack[-1]（弹出后的新栈顶）： 代表凹槽的左边界（左墙）
                        #i（当前遍历到的位置）： 代表凹槽的右边界（右墙）
                        #-height[top]：因为要减去池底厚度
                        while  m_stack and height[i]>height[m_stack[-1]]:
                            top=m_stack.pop()
                            if m_stack:
                                sum+=(i-m_stack[-1]-1)*(min(height[i],height[m_stack[-1]])-height[top])
                    m_stack.append(i)
     

        return sum
    
#20260723 看了一遍
            
