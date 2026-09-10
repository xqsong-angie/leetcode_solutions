class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        m_stack=[]
        res=[-1]*len(nums2)#代表nums2每一个元素的next greater element的下标，这里和739 daily temepratures 是一样的
        j=0
        for j in range(len(nums2)):#这里没有nums1的事，只对nums2操作，获取的是res
            if not m_stack:
                m_stack.append(j)
            else:
                if nums2[j]<=nums2[m_stack[-1]]:#递增栈，栈口小栈底大
                    m_stack.append(j)
                else:
                    res[m_stack[-1]]=j-m_stack[-1]
                    m_stack.pop()
                    while m_stack and nums2[j]>nums2[m_stack[-1]]:
                        res[m_stack[-1]]=j-m_stack[-1]
                        m_stack.pop()
                    m_stack.append(j)


        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:#更新ans
                    if res[j] != -1:#如果更新过
                        ans[i] = nums2[j + res[j]]#因为res[j]找的是相对j之后隔几个找到的next greater element
                    else:#这里可以不要，已经被初始化过了
                        ans[i] = -1

        return ans

#20260723 看了一遍
