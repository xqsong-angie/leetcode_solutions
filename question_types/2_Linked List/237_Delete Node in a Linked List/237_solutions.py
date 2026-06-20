#20260619
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:#没有办法看head，但是可以看node之后的节点
            node.val=node.next.val #把node改成下一个节点值
            node.next=node.next.next #再删掉下一个节点