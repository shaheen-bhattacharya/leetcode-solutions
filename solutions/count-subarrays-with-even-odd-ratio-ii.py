class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)
    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i
    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        #bx <= ay
        #ay - bx >= 0
        #s - p >= 0
        n = len(nums)
        for i in range(n):
            nums[i] = -b if nums[i] % 2 == 0 else a
        
        pref = list(accumulate(nums))
        # print(nums)
        # print(pref)
        snum = list(sorted(set(pref)))
        sn = len(snum)
        corr = {snum[i]:i+1 for i in range(sn)}
        # print(corr)
        ft = FenwickTree(sn+1)

        res = 0
        for v in pref:
            res += ft.query(corr[v])
            ft.update(corr[v], 1)

        return res

