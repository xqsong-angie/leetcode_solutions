#20260619
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i=list1
        j=list2
        merged=ListNode(val=-101)
        k=merged
        while i and j:
            if i.val<=j.val:
                k.next=i
                i=i.next
            else:
                k.next=j
                j=j.next
            k=k.next
        while i:
            k.next=i
            i=i.next
            k=k.next
        while j:
            k.next=j
            j=j.next
            k=k.next
        return merged.next

        