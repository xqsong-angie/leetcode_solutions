#20260801
#错：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        offset=1
        #get length
        cur=head
        length=0
        while cur.next:
            length+=1
            cur=cur.next
        length+=1
        cur.next=head#成环
        cur=head
        temp=head#下一个节点
        loop=length//2
        if cur:
            while offset<loop:
                for _ in range(length-offset):
                    temp=temp.next
                cur.next=temp
                cur=cur.next
                offset+=1
                for _ in range(offset):
                    temp=temp.next
                cur.next=temp
                cur=cur.next #🔥最后要把环断开，因为最后inplace返回，读结果的时候读到一个环卡住了造成memory limit exceeded

#对：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 第一步：快慢指针找中点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 此时 slow 就是前半段的尾巴，slow.next 是后半段的头
        second = slow.next
        slow.next = None  # 关键点：将前后两半断开，防止出现环！

        # 第二步：反转后半段链表
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 第三步：合并两个单链表
        # first 指向前半段头，second_head (也就是此时的 prev) 指向反转后的后半段头
        first = head
        second = prev
        while second:
            # 记录双方的下一个节点
            nxt1 = first.next
            nxt2 = second.next
            
            # 穿插链接
            first.next = second
            second.next = nxt1
            
            # 指针往后移动
            first = nxt1
            second = nxt2

                
        