class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] >= nums[i-1]:
            i += 1

        head = Node(-inf)
        tail = Node(inf)
        head.next = tail
        tail.prev = head
        curr = head 
        for i in range(len(nums)):
            node = Node(nums[i])
            curr.next = node
            node.prev = curr
            node.next = tail
            tail.prev = node
            curr = curr.next

        ops = 0
        heap = []
        curr = head.next
        bad = 0

        while curr.next != tail:
            if curr.next.val < curr.val:
                bad += 1
            heapq.heappush(heap, (curr.val + curr.next.val, curr))
            curr = curr.next

        if bad == 0:
            return ops

        while heap:
            tot, nd = heapq.heappop(heap)
            if (not nd.next) or nd.next == tail or tot != nd.val + nd.next.val:
                continue
            rem = 0
            if nd.val > nd.next.val:
                rem += 1
            if nd.prev != head and nd.val < nd.prev.val:
                rem += 1
            if nd.next.next != tail and nd.next.next.val < nd.next.val:
                rem += 1
            nd.val = tot
            nxt = nd.next
            nxt.next.prev = nd
            nd.next = nxt.next
            if nd.next != tail:
                heapq.heappush(heap, (nd.val + nd.next.val, nd))
            if nd.prev != head:
                heapq.heappush(heap, (nd.prev.val + nd.val, nd))

            if nd.next != tail and nd.val > nd.next.val:
                rem -= 1
            if nd.prev != head and nd.prev.val > nd.val:
                rem -= 1
            bad -= rem
            ops += 1
            if bad == 0:
                return ops
        return ops

            

            

            
            
            
            
        