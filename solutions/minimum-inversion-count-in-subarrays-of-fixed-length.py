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
            i -= i&-i
        return res
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ss = list(sorted(set(nums)))
        corr = {ss[i-1]:i for i in range(1, len(ss)+1)}
        ft = FenwickTree(len(ss)+2)

        tmp = 0 
        for i in range(k):
            tmp += i-ft.query(corr[nums[i]]-1)
            ft.update(corr[nums[i]], 1)
        res = tmp
        print(tmp)

        for i in range(k, n):
            ql = ft.query(corr[nums[i-k]] - 1)
            # if i == k:
            #     print(ql)
            # qg = k - 1 - ql
            tmp -= ql
            ft.update(corr[nums[i-k]], -1)
            ft.update(corr[nums[i]], 1)
            tmp += k - 1 - ft.query(corr[nums[i]]-1)
            res = min(res, tmp)
        return res



