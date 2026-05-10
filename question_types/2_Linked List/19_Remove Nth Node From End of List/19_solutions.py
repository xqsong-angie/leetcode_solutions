# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        dummy=ListNode(val=-1,next=head)
        cur=head
        count=1
        while cur.next!=None:
            cur=cur.next
            count+=1
        if not head:
            return head
        elif count<n:
            return head
        elif count==n:
            return head.next
        else:
            for _ in range(n):
                if fast.next==None:
                    return head
                fast=fast.next
            while fast.next!=None:
                slow=slow.next
                fast=fast.next
            temp=slow.next
            slow.next=temp.next
            if temp.next:   
                temp.next=None
            return dummy.next
            
        
