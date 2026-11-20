import random
from math import inf

class Node:
    def __init__(self, val=-1):
        self.next = None
        self.down = None
        self.up = None
        self.prev = None
        self.val = val


class Skiplist:
    def __init__(self):
        self.head = Node()
        self.tail = Node(inf)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.mel = 16

        ph = self.head
        pt = self.tail

        for _ in range(self.mel):
            ch = Node()
            ct = Node(inf)

            ch.next = ct
            ct.prev = ch

            ch.down = ph
            ph.up = ch

            ct.down = pt
            pt.up = ct

            ph, pt = ch, ct

        self.toph = ph

    def search(self, target: int) -> bool:
        cur = self.toph

        while cur:
            while cur.next and cur.next.val < target:
                cur = cur.next

            if cur.next and cur.next.val == target:
                return True

            cur = cur.down

        return False

    def add(self, num: int) -> None:
        update = []
        cur = self.toph

        while cur:
            while cur.next and cur.next.val < num:
                cur = cur.next

            update.append(cur)
            cur = cur.down

        prev = update[-1]
        nxt = prev.next

        node = Node(num)
        node.prev = prev
        node.next = nxt

        prev.next = node
        nxt.prev = node

        level = 0

        while random.random() < 0.5 and level < self.mel:
            level += 1

            prev = update[-1 - level]
            nxt = prev.next

            upper = Node(num)
            upper.down = node
            node.up = upper

            upper.prev = prev
            upper.next = nxt

            prev.next = upper
            nxt.prev = upper

            node = upper

    def erase(self, num: int) -> bool:
        cur = self.toph

        while cur:
            while cur.next and cur.next.val < num:
                cur = cur.next

            if cur.next and cur.next.val == num:
                node = cur.next

                while node:
                    prev = node.prev
                    nxt = node.next

                    prev.next = nxt
                    nxt.prev = prev

                    node = node.up

                return True

            cur = cur.down

        return False