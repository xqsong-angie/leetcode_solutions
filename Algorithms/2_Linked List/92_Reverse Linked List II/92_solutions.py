#20260731
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=[]
        left_node=right_node=None
        cur=head
        i=1
        while cur:
            if i==left:
                left_node=cur
            if i==right:
                right_node=cur
            if left_node and right_node:
                break
            cur=cur.next
            i+=1

        cur=left_node
        while cur!=right_node:
            temp.append(cur.val)
            cur=cur.next
        temp.append(cur.val)
        temp=temp[::-1]
        cur=left_node
        i=0
        while cur!=right_node:
            cur.val=temp[i]
            cur=cur.next
            i+=1
        cur.val=temp[i]
        return head