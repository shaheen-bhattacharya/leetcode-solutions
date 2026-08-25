class Allocator:

    def __init__(self, n: int):
        self.free = SortedList([(0, n-1)])
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for i, (s, e) in enumerate(self.free):
            if e - s + 1 >= size:
                self.free.pop(i)
                if s + size <= e:
                    self.free.add((s+size, e))
                self.blocks[mID].append((s, s+size-1))
                return s
        return -1

    def freeMemory(self, mID: int) -> int:
        amt = 0
        for s, e in self.blocks[mID]:
            amt += e - s + 1
            i = self.free.bisect_left((s, e))
            ps, pe = -1, -1
            ns, ne = -1, -1
            if i > 0:
                ps, pe = self.free[i-1]
                self.free.pop(i-1)
                i -= 1
            if i < len(self.free):
                ns, ne = self.free[i]
                self.free.pop(i)

            if (ps, pe) != (-1, -1):
                if pe != s - 1:
                    self.free.add((ps, pe))
                else:
                    s, e = ps, e

            if (ns, ne) != (-1, -1):
                if ns != e + 1:
                    self.free.add((ns, ne))
                else:
                    s, e = s, ne
            self.free.add((s, e))

        del self.blocks[mID]
        return amt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)