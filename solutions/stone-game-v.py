class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] + list(accumulate(stoneValue))
        dp = [[0] * n for _ in range(n)]
        lmax = [[0] * n for _ in range(n)]
        rmax = [[0] * n for _ in range(n)]
        lpos = [[-1] * n for _ in range(n)]
        rpos = [[-1] * n for _ in range(n)]
        for l in range(n):
            lp = l - 1
            rp = l
            for r in range(l+1, n):
                tot = pref[r+1] - pref[l]

                while lp + 1 < r:
                    lsum = pref[lp+2] - pref[l]
                    if lsum * 2 > tot:
                        break
                    lp += 1
                lpos[l][r] = lp

                while rp < r:
                    lsum = pref[rp+1] - pref[l]
                    if lsum * 2 >= tot:
                        break
                    rp += 1
                rpos[l][r] = rp

        for i in range(n):
            lmax[i][i] = stoneValue[i]
            rmax[i][i] = stoneValue[i]

        for length in range(2, n+1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                res = 0
                best = 0
                if lpos[l][r] >= l:
                    best = max(best, lmax[l][lpos[l][r]])
                else:
                    best = max(best, rmax[rpos[l][r]+1][r])
                dp[l][r] = best
                tot = pref[r+1] - pref[l]
                lmax[l][r] = max(lmax[l][r-1], tot + dp[l][r])
                rmax[l][r] = max(rmax[l+1][r], tot + dp[l][r])
                
        return dp[0][n-1]
        