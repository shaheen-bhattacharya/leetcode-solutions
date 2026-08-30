class Node:
    def __init__(self, site):
        self.next = None
        self.prev = None
        self.site = site
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = Node(url)
        self.head.next = node
        node.prev = self.head
        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr and steps > 1:
            self.curr = self.curr.prev
            steps -= 1
        if not self.curr:
            self.curr = self.head
        return self.curr.site

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 1:
            self.curr = self.curr.next 
            steps -= 1
        return self.curr.site

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)