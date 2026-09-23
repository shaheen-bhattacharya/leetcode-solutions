class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = [] 
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, -90))
        events.sort()

        heap = []
        res = []
        prev = 0

        i = 0
        while i < len(events):
            l, nh, r = events[i]
            while i < len(events) and events[i][0] == l:
                _, tnh, tr = events[i]
                heapq.heappush(heap, (tnh, tr))
                i += 1

            while heap and heap[0][1] <= l:
                heapq.heappop(heap) 
            
            if heap:
                curr = -heap[0][0]
            else:
                curr = 0
            if curr != prev:
                res.append((l, curr))
                prev = curr
        return res