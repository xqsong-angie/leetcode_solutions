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
        
#20260605
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#https://walkccc.me/LeetCode/problems/142/#__tabbed_1_3
"""
数学证明：
设起始到环入口为a, 环入口到快慢指针第一次相遇为b, 环中剩下部分为c,则
2(a+b)=a+n(b+c)+b
左右两侧同时减a+b得：a+b=n(b+c)
等式右边拆出一个b+c得：a+b=(n-1)(b+c)+b+c
等式两边同时减去b得：a=(n-1)(b+c)+c
此时把慢指针放回head, 就会在快指针转整数圈后再走c，与慢指针在环入口相遇
"""
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next#x1
      fast = fast.next.next#x2
      if slow == fast:#相遇位
        slow = head#慢指针移回开头
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    return None
  
#20260709看了一遍

#20260731 这个过了，但还是上面的逻辑更好
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        else:
            slow=head.next
            fast=head.next.next
            while slow!=fast:
                if not slow or not fast or not fast.next:
                    return None
                slow=slow.next
                fast=fast.next.next
            slow=head
            while slow!=fast:
                if not slow or not fast:
                    return None
                slow=slow.next
                fast=fast.next
            return slow


