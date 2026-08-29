class MyHashMap:

    def __init__(self):
        self.size = 16
        self.buckets = [[] for _ in range(self.size)]
        self.nums = 0
    
    def resize(self):
        self.size *= 2
        tmp = [[] for _ in range(self.size)]

        for b in buckets:
            for k, v in b:
                h = hash(k) % self.size
                tmp[h].append((k, v))

    def put(self, key: int, value: int) -> None:
        h = hash(key) % self.size
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))
        self.nums += 1
        if self.nums/self.size >= 0.75:
            resize()
 
    def get(self, key: int) -> int:
        h = hash(key) % self.size
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = hash(key) % self.size
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)