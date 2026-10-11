class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * n
    def update(self, i, delta):
        while i < self.n:
            self.bit[i] += delta
            i += i&-i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i&-i
        return res

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        res = 0
        n = len(instructions)
        ft = FenwickTree(max(instructions)+1)
        MOD = 1_000_000_007
        res = 0
        for i in range(n):
            ft.update(instructions[i], 1)
            res += min(ft.query(instructions[i]-1), i+1-ft.query(instructions[i])) % MOD
        return res % MOD

