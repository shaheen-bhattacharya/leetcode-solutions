# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        start = dummy
        while start:
            count = 0
            btmp = start
            tmp = start.next
            while tmp and count < k:
                print(tmp.val, count)
                count += 1
                btmp = tmp
                tmp = tmp.next
                print(" ")
            if count < k:
                return dummy.next
            # print(btmp.val, tmp.val)
            prev = tmp
            cur = start
            for _ in range(k-1):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            start = tmp
        return dummy.next
            
