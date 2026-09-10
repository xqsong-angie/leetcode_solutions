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
            
#20260605
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1:
            cur=head
            if not head.next:
                return None
            while cur.next.next:
                cur=cur.next
            cur.next=None
        
        else:
            #get list length
            cur=head
            count=0
            while cur:
                count+=1
                cur=cur.next
            diff=count-n
            if diff==0:
                return head.next
            else:
                #initialize pointers
                dummy=ListNode(val=-1)
                dummy.next=head
                prev=dummy
                cur=prev.next
                next=cur.next

                #move pointers
                for _ in range(diff):
                    prev=prev.next
                    cur=prev.next
                    next=cur.next
                prev.next=next
                cur.next=None

        return head
