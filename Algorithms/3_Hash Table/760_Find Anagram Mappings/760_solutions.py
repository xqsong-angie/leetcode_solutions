#20260803
from typing import (
    List,
)

from collections import defaultdict
class Solution:
    """
    @param a: lists A
    @param b: lists B
    @return: the index mapping
    """
    def anagram_mappings(self, a: List[int], b: List[int]) -> List[int]:
        # Write your code here
        P=[0]*len(a)
        hash_B=defaultdict(int)
        for i in range(len(b)):
            hash_B[b[i]]=i
        for i in range(len(a)):
            P[i]=hash_B[a[i]]
        return P