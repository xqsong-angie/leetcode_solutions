class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        m_stack=[]
        for i in range(n*2):#这里是在daily temperature基础上做一个circular的变形，两遍就够了，只要保证第一遍的尾能接上第二遍的头就行
            if not m_stack:
                m_stack.append(i%n)
            else:
                if nums[i%n]<=nums[m_stack[-1]]:
                    m_stack.append(i%n)
                else:
                    res[m_stack[-1]]=nums[i%n]
                    m_stack.pop()
                    while m_stack and nums[i%n]>nums[m_stack[-1]]:
                        res[m_stack[-1]]=nums[i%n]
                        m_stack.pop()
                    m_stack.append(i%n)
        return res
    
#20260723 看了一遍

#20260809
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        m_stack=[]
        for i in range(2*n):
                while m_stack and nums[i%n]>nums[m_stack[-1]]:
                    top=m_stack.pop()
                    res[top]=nums[i%n]
                m_stack.append(i%n)
            
        return res