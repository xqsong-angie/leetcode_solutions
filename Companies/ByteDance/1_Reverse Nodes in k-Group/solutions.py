class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def solution(self,head,k):
        if not head or not head.next or k<=1:
            return head
        else:
            length=0
            cur=head
            while cur.next:
                length+=1
                cur=cur.next

            prev=head
            cur=prev.next
            nxt=cur.next
            while length>1:

                while k:
                    if prev==head:
                        prev.next=None
                    cur.next=prev

                length-=k


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solution(self, head: Node, k: int) -> Node:
        if not head or not head.next or k <= 1:
            return head

        dummy = Node(0)
        dummy.next = head
        
        # group_prev 始终指向当前待反转组的前一个节点
        group_prev = dummy #🔥用dummy.next作为新的head

        while True:
            # 1. 检查当前组是否有节点需要反转
            curr = group_prev.next
            if not curr:
                break

            # 2. 找到当前组的尾节点（如果剩余不足 k 个，就以最后一个有效节点为尾）
            tail = group_prev
            for _ in range(k):
                if tail.next:
                    tail = tail.next
                else:
                    break  # 剩余不足 k 个，tail 停在链表末尾

            # 记录下一组的起始节点
            next_group = tail.next

            # 3. 反转从 curr 到 tail 的节点,🔥tail成为该段头，curr成为尾
            prev = next_group#🔥先把头尾指向做好，再逐一反转中间
            p = curr#p means present
            while p != next_group:
                nxt = p.next
                p.next = prev
                prev = p
                p = nxt

            # 4. 把上一组的尾巴连接到当前组反转后的新头节点（即原来的 tail）
            # 注意：在第一轮循环时，这里会把 dummy.next 更新为第一组反转后的头节点！
            group_prev.next = tail
            
            # 5. 将 group_prev 移动到当前组反转后的尾节点（即原来的 curr），准备处理下一组
            group_prev = curr

        # dummy.next 即为第一组反转后的头节点（整个链表的新头）
        return dummy.next
    
