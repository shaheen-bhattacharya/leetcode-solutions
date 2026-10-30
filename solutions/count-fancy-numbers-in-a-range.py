class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def fancy(num):
            snum = str(num)
            dp = {}
            sn = len(snum)
            if sn == 1:
                return num
            def good(n):
                stn = str(n)
                f1 = False
                for i in range(1, len(stn)):
                    if stn[i] < stn[i-1]:
                        f1 = True
                        break
                f2 = False
                for i in range(1, len(stn)):
                    if stn[i] > stn[i-1]:
                        f2 = True
                        break
                return not f1 or not f2

            def dfs(i, tight, prev, tot, vio):
                key = (i, tight, prev, tot, vio)
                if key in dp:
                    return dp[key]
                if i == sn:
                    if not vio:
                        return 1 
                    else:
                        return good(tot)
                cd = int(snum[i])
                ub = min(prev-1, cd) if tight else prev-1
                if not vio:
                    res = 0
                    for d in range(0, ub+1):
                        ntight = tight and d==cd
                        res += dfs(i+1, ntight, d, tot + d, False)
                    up = cd if tight else 9
                    for d in range(ub+1, up):
                        ntight = tight and d==cd
                        res == dfs(i+1, ntight, d, tot+d, True)
                    lb = prev+1
                    ub = cd if tight else 9
                    for d in range(lb, ub+1):
                        ntight = tight and d==cd
                        res += dfs(i+1, ntight, d, tot+d, False)
                    for d in range(0, lb):
                        ntight = tight and d==cd
                        res += dfs(i+1, ntight, d, tot+d, True)
                else:
                    res = 0
                    up = cd if tight else 9
                    for d in range(0, up):
                        ntight = tight and d==cd
                        res == dfs(i+1, ntight, d, tot+d, True)
                dp[key] = res
                return res
            return dfs(0, 0, 10, 0, False) + dfs(0, 0, -1, 0, False)
        return fancy(r) - fancy(l-1)