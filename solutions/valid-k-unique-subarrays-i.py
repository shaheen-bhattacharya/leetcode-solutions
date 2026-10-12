class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * n
    def update(self, i, delta):
        while i <= n:
            self.bit[i] += delta
            i += i&-i
    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i&-i
        return res
class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        """
        toggle from 1:odd 0: even 
        """        
        n = len(nums)
        maxv = max(nums)
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort()
        print(qs)
        # ft = FenwickTree()
