class Solution:
    class LinkedListNode:
        def __init__(self,val):
            self.val=val
            self.next=None

    def condense(self,head):
        myset=set()
        if head.next:
            prev=head#🔥head的值没有加入
            cur=head.next
            while cur:
                if cur.val in myset:
                    prev.next=cur.next
                else:
                    myset.add(cur.val)
                prev=prev.next#🔥prev如果刚删过节点，prev指针不能移动，万一下一个也要删呢
                cur=prev.next
        return head

#对：
class Solution:

    class LinkedListNode:

        def __init__(self, val):
            self.val = val
            self.next = None

    def condense(self, head: LinkedListNode) -> LinkedListNode:
        if not head:
            return None

        myset = set()
        # 1. 记得把 head 的值先加入 set
        myset.add(head.val)

        prev = head
        cur = head.next

        while cur:
            if cur.val in myset:
                # 2. 发现重复节点：跳过 cur，prev 指针原地不动
                prev.next = cur.next
            else:
                # 3. 未重复节点：加入 set，prev 正常前进一步
                myset.add(cur.val)
                prev = cur

            # 4. cur 始终更新为 prev 的下一个节点
            cur = prev.next

        return head