# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #把列表变成数组再判断
        cur=head
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next
        i=0
        n=len(res)
        j=n-1
        while i<j:
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True
            


