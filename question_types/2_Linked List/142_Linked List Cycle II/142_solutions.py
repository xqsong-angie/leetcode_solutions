# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif head.next==None:
            return None
        else:
            s=head
            f=head
            start=head
            meet=None
            while True:
                if f!=None and f.next!=None:
                    f=f.next.next
                    s=s.next
                    if s==f:
                        meet=s
                        break
                else:
                    return None

            while start!=meet:
                start=start.next
                meet=meet.next

            return start