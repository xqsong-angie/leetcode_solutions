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

#20260601
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         else:
#             prev=head
#             cur=head.next
#             while cur:
#                 next=cur.next
#                 cur.next=prev
#                 prev.next=None #会斩断数组，使prev连接不上之前的节点
#                 prev=cur
#                 cur=next
#             return prev
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            next_node = cur.next  # 1. 临时保存下一个节点，防止“迷路”
            cur.next = prev       # 2. 核心：调转方向！让当前节点指向前一个
            prev = cur            # 3. prev 前进一步
            cur = next_node       # 4. cur 前进一步
            
        return prev

