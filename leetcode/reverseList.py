# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fir = head
        temp= ListNode(head.val)
        while fir.next:
            fir=fir.next
            temp = ListNode(fir.val,temp)
        return temp