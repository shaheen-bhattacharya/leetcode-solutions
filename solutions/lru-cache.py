class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.corr = {}

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.corr:
            return -1
        node = self.corr[key]
        self.remove(node)
        self.insert(node)

    def put(self, key: int, value: int) -> None:
        if key in self.corr:
            node = self.corr[key]
            self.remove(node)
            node.val = value
        else:
            self.corr[key] = Node(key, value)
        node = self.corr[key]
        self.insert(node)
        if len(self.corr) > self.capacity:
            rnode = self.head.next
            k = rnode.key
            self.remove(rnode)
            del self.corr[k]
        





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)