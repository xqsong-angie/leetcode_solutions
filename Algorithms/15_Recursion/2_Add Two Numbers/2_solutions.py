#20260726 自己做出来了就是慢
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.head=ListNode(val=0)
        pt=self.head
        def addNumbers(l1,l2,pt):
            res=0
            if not l1 and not l2:
                return
            elif not l2:
                res=pt.val+l1.val
            elif not l1:
                res=pt.val+l2.val
            else:
                res=pt.val+l1.val+l2.val
            split=res%10
            pt.val=split

            if res>split:
                pt.next=ListNode(val=(res-split)//10)
            elif l1 and l1.next or l2 and l2.next:
                pt.next=ListNode(val=0)
                
            if l1 and l2:
                addNumbers(l1.next,l2.next,pt.next)
            elif not l1 and l2:
                addNumbers(None,l2.next,pt.next)
            elif not l2 and l1:
                addNumbers(l1.next,None,pt.next)
        addNumbers(l1,l2,pt)
        return self.head
