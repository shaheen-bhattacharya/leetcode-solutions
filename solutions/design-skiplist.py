class Node:
    def __init__(self, val=-float("inf"), layers=16):
        self.next = [None]*layers 
        self.val = val

class Skiplist:

    def __init__(self):
        self.head = Node()
        self.levels = 16

    def upgrades(self):
        amt = 1
        while amt < self.levels and random.random() < 0.5:
            amt += 1
        return amt

    def search(self, target: int) -> bool:
        curr = self.head
        for lvl in range(self.levels-1, -1, -1):
            while curr.next[lvl] and curr.next[lvl].val < target:
                curr = curr.next[lvl]
            if curr.next[lvl] and curr.next[lvl].val == target:
                return True
        return False


    def add(self, num: int) -> None:
        curr = self.head
        node = Node(val=num)
        nxt = [None] * self.levels
        upg = self.upgrades()
        for lvl in range(self.levels-1, -1, -1):
            while curr.next[lvl] and curr.next[lvl].val < num:
                curr = curr.next[lvl]
            nxt[lvl] = curr
        
        for lvl in range(upg):
            node.next[lvl] = nxt[lvl].next[lvl]
            nxt[lvl].next[lvl] = node
        
    def erase(self, num: int) -> bool:
        prev = [None] * self.levels
        curr = self.head
        for lvl in range(self.levels-1, -1, -1):
            while curr.next[lvl] and curr.next[lvl].val < num:
                curr = curr.next[lvl]
            prev[lvl] = curr    

        need = prev[0].next[0]
        if not need or need.val != num:
            return False
        
        for lvl in range(self.levels):
            if not prev[lvl].next[lvl] or not prev[lvl].next[lvl].val == num:
                continue
            node = prev[lvl].next[lvl]
            prev[lvl].next[lvl] = node.next[lvl]
        return True





            

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)