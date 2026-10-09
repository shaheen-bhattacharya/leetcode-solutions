class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        tot = 0
        while i > 0:
            tot += self.tree[i]
            i -= i & -i
        return tot

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        maxv = max(nums)
        n = len(nums)
        ft = FenwickTree(n)
        nsort = sorted(nums)
        compress = {nsort[i]:i+1 for i in range(n)}
        res = []
        for num in nums[::-1]:
            ft.update(compress[num], 1)
            res.append(ft.query(compress[num]-1))
        return res