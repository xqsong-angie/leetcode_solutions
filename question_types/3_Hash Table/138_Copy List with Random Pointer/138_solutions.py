#20260803
#错：
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #此题不要用copy.deepcopy()
        if head:
            new_head=Node(head.val)
            cur=new_head#new_head的指针
            while cur and head:
                if head.next:
                    cur.next=Node(head.next.val)
                if head.random:
                    cur.random=Node(head.random.val)#🔥这里不应该建新节点，应该利用已有的节点
                cur=cur.next
                head=head.next
            return new_head
        else:
            return None
        
#对：有映射关系的时候首先想哈希
class Solution:

    def copyRandomList(
        self, head: "Optional[Node]"
    ) -> "Optional[Node]":
        if not head:
            return None

        # 1. 哈希表：原节点 -> 新节点
        node_map = {}

        # 2. 第一遍遍历：创建所有新节点，建立映射
        cur = head
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        # 3. 第二遍遍历：连接 next 和 random 指针
        cur = head
        while cur:
            # node_map[cur] 是当前的新节点
            # 如果原节点有 next，把新节点的 next 指向原节点 next 对应的新节点
            if cur.next:
                node_map[cur].next = node_map[cur.next]

            # 如果原节点有 random，同理指向对应的映射节点
            if cur.random:
                node_map[cur].random = node_map[cur.random]

            cur = cur.next

        # 返回原 head 映射对应的新 head
        return node_map[head]