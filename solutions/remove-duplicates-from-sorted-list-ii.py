# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-3)
        tmp = head
        prev = dummy
        prev.next = head
        while tmp:
            dv = tmp.val
            cur = tmp
            if cur.next and cur.next.val == dv:
                while cur and cur.val == dv:
                    cur = cur.next
                prev.next = cur
                tmp = cur 
            else:
                prev = prev.next 
                tmp = tmp.next
        return dummy.next
