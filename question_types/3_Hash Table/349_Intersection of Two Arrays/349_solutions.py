class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mydict={}
        mylist=[]
        for n1 in set(nums1):
            mydict[n1]=0
        for n2 in set(nums2):
            if n2 in mydict.keys():
                mydict[n2]+=1
        for k,v in mydict.items():
            if v>0:
                mylist.append(k)
        return mylist
