# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bad = set()
        tmp = head
        seen = set()
        while tmp:
            if tmp.val in seen:
                bad.add(tmp.val)
            else:
                seen.add(tmp.val)
            tmp = tmp.next
        
        print(bad)
        dummy = ListNode(-23)
        prev = dummy
        prev.next = head
        tmp = head
        while tmp:
            nxt = tmp.next
            if tmp.val in bad:
                prev.next = nxt
                tmp.next = None 
            tmp = nxt
        return dummy.next
