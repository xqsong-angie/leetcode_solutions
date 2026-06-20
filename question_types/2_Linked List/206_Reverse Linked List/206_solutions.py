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
class Solution: #这个是业界标准答案（prev设为head前面的空节点）
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            next_node = cur.next  # 1. 临时保存下一个节点，防止“迷路”
            cur.next = prev       # 2. 核心：调转方向！让当前节点指向前一个
            prev = cur            # 3. prev 前进一步
            cur = next_node       # 4. cur 前进一步
            
        return prev


#20260619 memory limit exceed
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            prev=head
            cur=head.next
            next=cur.next
            while next:
                cur.next=prev
                prev.next=None #这里会使链表断掉
                prev=cur
                cur=next
                next=cur.next
            cur.next=prev
            return cur
        else:
            return head
        
#正确：
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            prev = head
            cur = head.next
            nxt = cur.next  # 避免使用 Python 内置函数名 next
            
            # 原来的头节点反转后就是尾节点，它的 next 应该直接指向 None
            # 这一步在循环外只做一次！
            prev.next = None 
            
            while nxt:
                cur.next = prev  # 1. 翻转指针
                
                # 2. 三个指针整体向前移动
                prev = cur       
                cur = nxt        
                nxt = nxt.next   # 3. 此时的 nxt.next 才是干净的、没被修改过的下一个节点
                
            cur.next = prev  # 处理最后一个节点的指向
            return cur
        else:
            return head