class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 1_000_000_007
        n = len(value)
        def good(th):
            tot = 0
            ops = 0
            for i in range(n):
                if value[i] < th:
                    continue
                need = (value[i] - th)//decay[i] + 1
                if need > 0:
                    tot += value[i] * need - decay[i] * (need - 1) * need//2
                    ops += need
            return (tot, ops)
        
        maxv = max(value)
        l, r = 0, maxv + 1
        while l < r:
            mid = (l+r)//2
            if good(mid)[1] > m:
                l = mid + 1
            else:
                r = mid

        if l == 0:
            return good(l)[0] % MOD
        t, o = good(l)
        t -= (o-m) * (l-1)
        return t % MOD



                

            