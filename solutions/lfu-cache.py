class Node:
    def __init__(self, val, uses, key):
        self.val = val
        self.uses = uses
        self.next = None 
        self.prev = None
        self.key = key

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        def ml():
            head = Node(-1, -1, -1)
            tail = Node(-1, -1, -2)
            head.next = tail
            tail.prev = head
            return (head, tail)
        self.rmap = {}
        self.lls = defaultdict(ml)
        self.mu = 0
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.next = None
        node.prev = None
    
    def insert(self, node, key):
        head, tail = self.lls[key]
        prev = tail.prev
        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.rmap:
            return -1
        node = self.rmap[key]
        head, tail = self.lls[node.uses]
        self.remove(node)
        if self.mu == node.uses and head.next == tail:
            self.mu += 1
        node.uses += 1
        self.insert(node, node.uses)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.rmap:
            self.rmap[key] = Node(value, 1, key)
            self.mu = 1
            node = self.rmap[key]
            self.insert(node, 1)
        else:
            node = self.rmap[key]
            node.val = value
            self.remove(node)
            head, tail = self.lls[node.uses]
            if self.mu == node.uses and head.next == tail:
                self.mu += 1
            node.uses += 1
            self.insert(node, node.uses)

        if len(self.rmap) > self.capacity:
            head, tail = self.lls[self.mu]
            rnode = head.next
            del self.rmap[rnode.key]
            self.remove(rnode)
            if rnode.uses == self.mu and head.next == tail:
                self.mu += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)