class Allocator:

    def __init__(self, n: int):
        self.free = SortedList([(0, n-1)])
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for i, (s, e) in enumerate(self.free):
            if s - e + 1 >= size:
                self.free.pop(i)
                self.free.append((s+size, e))
                self.blocks[mID].append((s, s+size-1))
                return s
        return -1

    def freeMemory(self, mID: int) -> int:
        ns = len(self.blocks[mID])
        for s, e in self.blocks[mID]:
            i = self.free.bisect_left((s, e))
            self.free.pop(i-1)
            ps, pe = self.free[i-1]
            if pe >= s-1:
                pe = max(pe, e)
            if i == len(self.free):
                self.free.append((ps, pe))
            else:
                ns, ne = self.free[i+1]
                if pe > ns:
                    pe = max(pe, ne)
                self.free.append((ps, pe))                

        del self.blocks[mID]
        return ns



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)