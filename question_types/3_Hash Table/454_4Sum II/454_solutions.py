class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        mydict={}
        count=0
        for i in range(n):
            for j in range(n):
                if nums1[i]+nums2[j] not in mydict.keys():
                    mydict[nums1[i]+nums2[j]]=0
                mydict[nums1[i]+nums2[j]]+=1

        for k in range(n):
            for l in range(n):
                target=0-(nums3[k]+nums4[l])
                if target in mydict.keys():
                    count+=mydict[target]
        return count
    
#20260605
from typing import List
from collections import Counter

class Solution:
    #https://algo.monster/liteproblems/454
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # Create a hash map to store the frequency of all possible sums from nums1 and nums2
        # Key: sum of a pair (a, b) where a is from nums1 and b is from nums2
        # Value: frequency of this sum
        sum_count = Counter(a + b for a in nums1 for b in nums2)
      
        # For each pair (c, d) from nums3 and nums4, check if -(c + d) exists in the hash map
        # If it exists, add its frequency to the result
        # This works because we need a + b + c + d = 0, which means a + b = -(c + d)
        result = sum(sum_count[-(c + d)] for c in nums3 for d in nums4)
      
        return result
