# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fir = head
        sec=head.next
        while sec:
            if fir.val!=sec.val:
                fir=fir.next
                sec=sec.next
            else:
                while fir.val==sec.val:
                    if sec.next:
                        sec=sec.next
                    else:
                        break
                if fir.val==sec.val:
                    fir.next = None
                    sec=sec.next
                else:
                    fir.next=sec
                    fir=sec
                    sec=sec.next
        return head