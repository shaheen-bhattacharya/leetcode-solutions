class RandomizedSet:

    def __init__(self):
        self.corr = {} #idx: val
        self.rev = {} #val: idx
        self.ptr = 0

    def insert(self, val: int) -> bool:
        if val in self.rev:
            return False
        self.corr[self.ptr] = val 
        self.rev[val] = self.ptr
        self.ptr += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.rev:
            return False
        idx = self.rev[val]
        del self.corr[idx]
        del self.rev[val]
        last = self.ptr - 1
        nval = self.corr[last]
        del self.rev[nval]
        del self.corr[last]
        self.corr[idx] = nval
        self.rev[nval] = idx
        self.ptr -= 1
        return True

    def getRandom(self) -> int:
        x = random.randint(0, self.ptr-1)
        return self.corr[x]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()