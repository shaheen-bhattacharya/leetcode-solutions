class TreeAncestor:

    def __init__(self, n: int, parent: list[int]):
        LOG = n.bit_length()
        self.parent = parent
        self.up = [[-1]*(LOG) for _ in range(n)] #self.up[node][p] => 2^p ancestor
        for i in range(n):
            self.up[i][0] = parent[i]

        for node in range(n):
            for p in range(1, LOG):
                prev = self.up[node][p-1]
                if prev != -1:
                    self.up[node][p] = self.up[self.up[node][p-1]][p-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for p in range(k.bit_length()):
            if k & (1 << p):
                node = self.up[node][p]
                if node == -1:
                    return -1
        return node   


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)