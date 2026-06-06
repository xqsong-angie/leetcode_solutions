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

#20260605
class Solution:
    #https://www.w3schools.com/python/ref_list_sort.asp
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1=list(set(nums1))
        set_nums2=list(set(nums2))
        nums1_len=len(set_nums1)
        nums2_len=len(set_nums2)
        set_nums1.sort()
        set_nums2.sort()

        i=j=0
        res=[]
        while i<nums1_len and j<nums2_len:
            if set_nums1[i]==set_nums2[j]:
                res.append(set_nums1[i])
                i+=1
                j+=1
            elif set_nums1[i]<set_nums2[j]:
                i+=1
            else:
                j+=1
        return res