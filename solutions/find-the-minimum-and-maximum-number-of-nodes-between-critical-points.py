# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head.next 
        prev = head
        fst = -1
        sl = -1
        minv = inf
        
        i = 1
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if fst == -1:
                    fst = i
                else:
                    minv = min(minv, i - sl)
                sl = i
            prev = prev.next
            curr = curr.next
            i += 1
        if sl == -1 or minv == inf:
            return [-1, -1]
        return [minv, sl - fst]