#20260801
#错：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA=headA
        lengthA=0
        while curA:
            lengthA+=1
            curA=curA.next
        curB=headB
        lengthB=0
        while curB:
            lengthB+=1
            curB=curB.next
        curA=headA
        curB=headB
        if lengthA<lengthB:
            diff=lengthB-lengthA
            for _ in range(diff):
                curB=curB.next
        elif lengthA>lengthB:
            diff=lengthA-lengthB
            for _ in range(diff):
                curA=curA.next
        while curA!=curB or not curA or not curB:#🔥不要not curA or not curB，两个指针同时结束
            curA=curA.next
            curB=curB.next
        if curA==curB:
            return curA.val #🔥要返回的是节点不是值
        else:
            return 0


#对：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA=headA
        lengthA=0
        while curA:
            lengthA+=1
            curA=curA.next
        curB=headB
        lengthB=0
        while curB:
            lengthB+=1
            curB=curB.next
        curA=headA
        curB=headB
        if lengthA<lengthB:
            diff=lengthB-lengthA
            for _ in range(diff):
                curB=curB.next
        elif lengthA>lengthB:
            diff=lengthA-lengthB
            for _ in range(diff):
                curA=curA.next
        while curA!=curB:
            curA=curA.next
            curB=curB.next
        if curA==curB:
            return curA








