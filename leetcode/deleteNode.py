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
        delnode= node
        if delnode.next:
            delnode.val=delnode.next.val
            if delnode.next.next:
                delnode.next = delnode.next.next
            else:
                delnode.next=None