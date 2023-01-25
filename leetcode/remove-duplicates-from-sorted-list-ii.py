# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                fla=False
                ls = ListNode()
                las =ListNode()
                ls.next = las
                fir = head
                sec = head.next
                while sec :
                    if fla:
                        break
                    if fir.val != sec.val:
                        las.next=ListNode(fir.val)
                        las=las.next
                        if sec.next :
                            fir = fir.next
                            sec = sec.next
                        else:
                            las.next=ListNode(sec.val)
                            las=las.next
                            break
                    else:
                        while fir.val == sec.val:
                            if sec.next:
                                sec = sec.next
                            else:
                                fla=True
                                break
                        if sec.next:
                            fir = sec
                            sec = sec.next
                        else:
                            if not fla:
                                las.next=ListNode(sec.val)
                                las=las.next
                            break
                ls=ls.next.next
                return ls
            else:
                return head
        else:
            return head