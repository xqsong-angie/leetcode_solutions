# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=ListNode(val=-1)
        dummy_head.next=head

        if not head:
            return head
        else:
            cur=dummy_head
            while cur and cur.next:
                if cur.next.val==val:
                    cur.next=cur.next.next
                else:
                    cur=cur.next
                
        return dummy_head.next 
