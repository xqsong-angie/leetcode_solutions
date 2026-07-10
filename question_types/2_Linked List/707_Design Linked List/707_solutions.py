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
            for _ in range(index):#index有多少就移动几次指针
                if cur.next:#🔥这里其实是有问题的，如果空链表且index>0, cur==None, cur.next取不出来会直接崩溃，建议补充 if not cur return -1
                    cur=cur.next
                else:#index太大了，后面空了
                    return -1
            return cur.val if cur!=None else -1#空链表且index==0

    def addAtHead(self, val: int) -> None:
        new_head=ListNode(val) #待插入头
        new_head.next=self.head#连结头
        self.head=new_head#更新头

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val)#待插入尾
        if not self.head:
            self.head=new_node #没有头作为新头
        else:#有头，插入尾部
            cur=self.head
            while cur.next!=None:
                cur=cur.next#指针移动到尾部
            cur.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:#给定index插入节点
        if index==0:
            self.addAtHead(val)
        else:
            cur=self.head
            new_node=ListNode(val)#要插入到节点
            for _ in range(index-1):#到index前一个
                if cur:
                    cur = cur.next
                else:#说明index越界，不能加
                    return
            if not cur:#空头部，以及index在最后越界了：len(list)=4, index=5
                return
            temp=cur.next#有可能是一个节点，也可能为空，以免丢失cur.next先保存为temp
            new_node.next=temp
            cur.next=new_node

    def deleteAtIndex(self, index: int) -> None:
        if index==0 and not self.head:
            return
        elif index==0:#删头节点
            if self.head.next:
                self.head=self.head.next
            else:
                self.head=None
        else:#删一般节点
            cur=self.head
            for _ in range(index-1):#也还是到前一个位置
                if cur.next:
                    cur=cur.next
                else:
                    return
            if cur.next:#直接越过cur.next
                cur.next=cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#20260709看了一遍