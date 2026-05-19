class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        m_stack=[]
        res=[-1]*len(nums2)
        j=0
        for j in range(len(nums2)):
            if not m_stack:
                m_stack.append(j)
            else:
                if nums2[j]<=nums2[m_stack[-1]]:
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
                if nums1[i]==nums2[j]:
                    if res[j] != -1:
                        ans[i] = nums2[j + res[j]]
                    else:
                        ans[i] = -1

        return ans

        