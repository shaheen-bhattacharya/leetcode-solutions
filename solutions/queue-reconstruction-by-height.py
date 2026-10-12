class Node:
    def __init__(self, idx):
        self.next = None
        self.prev = None
        self.idx = idx

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        n = len(people)
        people.sort(key = lambda x: (-x[0], x[1]))
        # print(people)
        i = 0
        while i < n:
            curr = []
            h, k = people[i]
            num = h
            while i < n and people[i][0] == num:
                curr.append(i)
                i += 1
            j = 0
            tmp = self.head
            amt = 0
            while j < len(curr):
                pc = people[curr[j]]
                if amt == pc[1]:
                    nd = Node(curr[j])
                    nxt = tmp.next
                    tmp.next = nd
                    nd.prev = tmp
                    nd.next = nxt
                    nxt.prev = nd
                    j += 1
                amt += 1
                tmp = tmp.next
                # print(tmp.idx)
        res = []
        tmp = self.head.next
        while tmp != self.tail:
            res.append(people[tmp.idx])
            tmp = tmp.next
        return res


        

            

