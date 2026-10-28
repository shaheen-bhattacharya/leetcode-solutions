from collections import defaultdict
from math import inf

class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        cost = defaultdict(list)
        seen = set()

        for x in nums:
            if x in seen:
                continue
            seen.add(x)

            best = {x: 0}
            num = x
            ops = 0

            while num > 1:
                ops += 1
                num //= 2
                best[num] = min(ops, best.get(num, inf))

                tmp = num
                top = ops
                while tmp < sm:
                    tmp *= 2
                    top += 1
                    best[tmp] = min(top, best.get(tmp, inf))

            cost[x] = list(best.items())

        dp = [inf] * (sm + 1)
        dp[0] = 0

        for x in nums:
            ndp = dp[:]
            for v, c in cost[x]:
                if v > sm:
                    continue
                for s in range(v, sm + 1):
                    if dp[s - v] != inf:
                        ndp[s] = min(ndp[s], dp[s - v] + c)
            dp = ndp

        return dp[sm] if dp[sm] != inf else -1