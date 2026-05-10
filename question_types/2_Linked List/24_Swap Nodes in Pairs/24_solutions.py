# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            pre=head
            cur=head.next
            head=head.next
            dummy=None
            temp=None
            while cur!=None:
                temp=cur.next
                cur.next=pre
                pre.next=temp
                if dummy:
                    dummy.next=cur
                dummy=pre
                pre=temp
                if pre:
                    cur=pre.next
                else:
                    cur=None
            return head