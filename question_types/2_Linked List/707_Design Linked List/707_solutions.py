class ListNode:
    def __init__(self,val): 
        self.val=val
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if not self.head:
            return -1 
        cur=self.head
        for _ in range(index):
            if cur.next!=None:
                cur=cur.next
            else:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_head=ListNode(val=val)
        new_head.next=self.head
        self.head=new_head

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val=val)
        if not self.head:
            self.head=new_node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val=val)
        else:
            new_node=ListNode(val=val)
            if self.head:
                cur=self.head
                for _ in range(index-1):
                    if cur.next!=None:
                        cur=cur.next
                if not cur:
                    return#这里没用，所以这个代码能accept，但不对
                new_node.next=cur.next
                cur.next=new_node    


        
    def deleteAtIndex(self, index: int) -> None:
        if self.head:
            if index==0:
                self.head=self.head.next
            else:
                cur=self.head
                for _ in range(index-1):
                    if cur.next!=None:
                        cur=cur.next
                    else:
                        return
                if cur.next==None:
                    return 

                cur.next=cur.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


#20260528

class ListNode:
    def __init__(self,val): 
        self.val=val
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if index<0:
            return -1
        else:
            cur=self.head
            for _ in range(index):
                if cur.next:
                    cur=cur.next
                else:
                    return -1
            return cur.val if cur!=None else -1

    def addAtHead(self, val: int) -> None:
        new_head=ListNode(val)
        new_head.next=self.head
        self.head=new_head

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val)
        if not self.head:
            self.head=new_node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        else:
            cur=self.head
            new_node=ListNode(val)
            for _ in range(index-1):
                if cur:
                    cur = cur.next
                else:
                    return
            if not cur:
                return
            temp=cur.next
            new_node.next=temp
            cur.next=new_node

    def deleteAtIndex(self, index: int) -> None:
        if index==0 and not self.head:
            return
        elif index==0:
            if self.head.next:
                self.head=self.head.next
            else:
                self.head=None
        else:
            cur=self.head
            for _ in range(index-1):
                if cur.next:
                    cur=cur.next
                else:
                    return
            if cur.next:
                cur.next=cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)