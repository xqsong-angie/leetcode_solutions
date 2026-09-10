#20260801
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            cur=head
            length=0
            while cur.next:
                length+=1
                cur=cur.next
            length+=1
            cur.next=head#成环
            for _ in range(length-k%length):
                cur=cur.next
            new_head=cur.next
            cur.next=None
            return new_head 