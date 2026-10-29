class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        idxs = [0] * 7
        r, c = 0,0
        for i in range(1, 7):
            if directions[i-1] == "D":
                r += 1
            else:
                c += 1
            idxs[i] = r*4+c

        sl, sr = str(l-1), str(r)
        sl = "0"*(16-len(sl))+sl
        sr = "0"*(16-len(sr))+sr

        def good(snum):
            dp = {}
            sn = len(snum)
            def dfs(i, j, prev):
                key = (i, j, prev)
                if key in dp:
                    return dp[key]
                if i == sn:
                    return 1
                ub = prev if i == idxs[j] else 9
                nj = j
                if i == idxs[j]:
                    nj += 1
                ret = 0
                for d in range(prev+1):
                    nprev = prev if i == idxs[j] else d
                    ret += dfs(i+1, nj, nprev)
                dp[key] = ret
                return ret
            return dfs(0,0,9)
        return good(sr) - good(sl)
