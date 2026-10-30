class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        idxs = [0] * 7
        ro, c = 0,0
        for i in range(1, 7):
            if directions[i-1] == "D":
                ro += 1
            else:
                c += 1
            idxs[i] = ro*4+c

        sl, sr = str(l-1), str(r)
        # print(str(r))
        sl = "0"*(16-len(sl))+sl
        sr = "0"*(16-len(sr))+sr
        # print(sl)

        def good(snum):
            dp = {}
            sn = len(snum)
            def dfs(i, j, prev, tight):
                key = (i, j, prev, tight)
                if key in dp:
                    return dp[key]
                if i == sn:
                    return 1
                cd = int(snum[i])
                nj = j

                if tight:
                    if i == idxs[j]:
                        nj += 1
                        ub = min(prev, cd)
                    else:
                        ub = cd
                else:
                    if i == idxs[j]:
                        nj += 1
                        ub = prev
                    else:
                        ub = 9
                ret = 0
                for d in range(ub+1):
                    nprev = prev if i != idxs[j] else d
                    ntight = tight and d == cd
                    ret += dfs(i+1, nj, nprev, ntight)
                dp[key] = ret
                return ret
            return dfs(0,0,9,True)
        return good(sr) - good(sl)
