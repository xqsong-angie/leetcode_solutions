#20260801
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left_dummy = ListNode()
        right_dummy = ListNode()
      
        # Maintain pointers to build the two lists
        left_tail = left_dummy
        right_tail = right_dummy
      
        # Traverse the original linked list
        while head:
            if head.val < x:
                # Add current node to the left partition
                left_tail.next = head
                left_tail = left_tail.next
            else:
                # Add current node to the right partition
                right_tail.next = head
                right_tail = right_tail.next
          
            # Move to the next node
            head = head.next
      
        # Terminate the right partition to avoid cycles
        right_tail.next = None#🔥只是改变了 right_tail.next，节点 5 本身的 next 指针从未被修改过！ 它仍然保留着在原链表中的记忆，即：5.next = 最后一个2
      
        # Connect the left partition to the right partition
        left_tail.next = right_dummy.next
      
        # Return the head of the partitioned list (skip dummy node)
        return left_dummy.next
