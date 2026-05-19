class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        m_stack=[]
        for i in range(n*2):
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