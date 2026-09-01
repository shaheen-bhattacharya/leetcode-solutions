class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.corr = {}
        for e, p in events:
            self.corr[e] = p
            heapq.heappush(self.heap, (-p, e))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.corr[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            np, e = heapq.heappop(self.heap)
            if self.corr[e] == -np:
                continue
            return e
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()