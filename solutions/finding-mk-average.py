class MKAverage:

    def __init__(self, m: int, k: int):
        self.sl = SortedList()
        self.q = deque()
        self.tot = 0
        self.bad = 0
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        k = self.k
        self.tot += num
        self.q.append(num)
        if len(self.sl) < 2*k:
            self.sl.add(num)
            self.bad += num
            return

        idx = self.sl.bisect_left(num)
        if idx < k:
            self.bad += num
            self.bad -= self.sl[k-1]
        elif idx > len(self.sl) - k:
            self.bad += num
            self.bad -= self.sl[len(self.sl) - k]
        self.sl.add(num)

        if len(self.q) > self.m:
            rem = self.q.popleft()
            idx = self.sl.bisect_left(rem)
            if idx < k:
                self.bad -= rem
                self.bad += self.sl[k]
            elif idx >= len(self.sl) - k:
                self.bad -= rem
                self.bad += self.sl[len(self.sl) - k - 1]
            self.sl.remove(rem)
            self.tot -= rem
        
    def calculateMKAverage(self) -> int:
        # print(self.tot, self.bad, self.sl)
        return (self.tot - self.bad) // (self.m - 2*self.k) if len(self.sl) >= self.m else -1


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()