class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def good(num):
            snum = str(num)
            sn = len(snum)
            dp = {}
            def dfs(i, used, tight, tot):
                key = (i, used, tight, tot)
                if key in dp:
                    return dp[key]
                if i == sn:
                    return 1 if used >= 2 and tot == 0 else 0
                cd = int(snum[i])
                ub = cd if tight else 9
                res = 0
                for d in range(ub+1):
                    ntight = tight and d == cd
                    nused = used if used == 0 and d == 0 else used + 1
                    ntot = tot - d if d % 2 == 0 else tot + d
                    res += dfs(i+1, nused, ntight, ntot)
                dp[key] = res
                return res
            return dfs(0, 0, True, 0)
        return good(high) - good(low - 1)

                
