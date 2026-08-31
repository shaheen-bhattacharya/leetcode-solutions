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
        snd = -1
        sl = -1
        i = 1
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                print(curr.val)
                if fst == -1:
                    fst = i
                elif snd == -1:
                    snd = i
                sl = i
            prev = prev.next
            curr = curr.next
            i += 1
        if snd == -1:
            return [-1, -1]
        return [snd - fst, sl - fst]