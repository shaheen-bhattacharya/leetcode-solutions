from sortedcontainers import SortedList
from collections import defaultdict


class Allocator:

    def __init__(self, n: int):
        # (start, end) inclusive free intervals
        self.free = SortedList([(0, n - 1)])

        # mID -> [(start, end), ...]
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        # Need the leftmost free interval with enough space
        for i, (s, e) in enumerate(self.free):
            if e - s + 1 >= size:

                # Remove old interval
                self.free.pop(i)

                # Allocate [s, s + size - 1]
                alloc_end = s + size - 1

                # Remaining free space
                if alloc_end < e:
                    self.free.add((alloc_end + 1, e))

                self.blocks[mID].append((s, alloc_end))

                return s

        return -1

    def freeMemory(self, mID: int) -> int:
        ans = 0

        for s, e in self.blocks[mID]:
            ans += e - s + 1

            # Find where this interval should go
            idx = self.free.bisect_left((s, e))

            # Merge with previous free interval
            if idx > 0:
                ps, pe = self.free[idx - 1]

                if pe + 1 == s:
                    s = ps
                    self.free.pop(idx - 1)
                    idx -= 1

            # Merge with next free interval
            if idx < len(self.free):
                ns, ne = self.free[idx]

                if e + 1 == ns:
                    e = ne
                    self.free.pop(idx)

            self.free.add((s, e))

        del self.blocks[mID]

        return ans