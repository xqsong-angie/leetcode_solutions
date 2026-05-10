# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, pre:Optional[ListNode],cur:Optional[ListNode])-> Optional[ListNode]:
        temp=None        
        if cur is None:
            return pre
        if cur!=None:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
            return self.reverse(pre,cur)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative
        # if not head:
        #     return head
        # else:
        #     cur=head
        #     pre=None
        #     temp=None
        #     while cur!=None:
        #         temp=cur.next
        #         cur.next=pre
        #         pre=cur
        #         cur=temp
        #     return pre
        #recursive
        if not head or not head.next:
            return head

        cur=head
        pre=None
        return self.reverse(pre,cur)


