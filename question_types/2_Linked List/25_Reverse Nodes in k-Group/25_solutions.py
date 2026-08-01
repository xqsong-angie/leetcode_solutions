#20260731
#错：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        #先获取链表总长
        length=0
        while cur:
            length+=1
            cur=cur.next
        def reverseAtPt(node,pt):
            prev=node
            cur=prev.next
            nxt=cur.next
            for _ in range(k-1):
                cur.next=prev
                prev.next=None #🔥这里把两段之间的连接斩断了
                prev=cur
                cur=nxt
                nxt=nxt.next#🔥nxt可能为空指针
            if length-(pt+k-1)>=k:
                prev.next=reverseAtPt(cur,pt+k) #🔥prev是翻转后的新头节点
                return prev
            else:#上个尾和下个头相连
                return head#🔥这里应该返回node
        return reverseAtPt(head,1)
    
#对：
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 获取链表总长度
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        # 2. 递归翻转函数：count 代表当前剩余节点数
        def reverseAtPt(node, count):
            # 如果剩余节点不足 k 个，无需翻转，直接返回当前头节点
            if count < k:
                return node
            
            # 标准双指针/三指针翻转当前 k 个节点
            prev = None #🔥prev设成None才不会有死循环
            cur = node
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            # 翻转完成后：
            # prev 是当前组的新头节点
            # node 变成了当前组的新尾节点
            # cur 是下一组的起始节点
            
            # 将当前组的尾节点链接到下一组翻转后的头节点
            node.next = reverseAtPt(cur, count - k)
            
            # 返回当前组翻转后的新头节点
            return prev

        return reverseAtPt(head, length)