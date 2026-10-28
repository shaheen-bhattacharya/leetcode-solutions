from itertools import accumulate

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

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
        n = len(nums)

        for i in range(n):
            nums[i] = -b if nums[i] % 2 == 0 else a

        pref = [0] + list(accumulate(nums))

        snum = sorted(set(pref))
        corr = {v: i + 1 for i, v in enumerate(snum)}

        ft = FenwickTree(len(snum))

        res = 0
        for v in pref:
            idx = corr[v]
            res += ft.query(idx)
            ft.update(idx, 1)

        ec = 0
        for v in nums:
            if v == -b:
                ec += 1
                res -= ec
            else:
                ec = 0

        return res