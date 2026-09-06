class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        #yrtxhrcbaterrt abcuitiutgu
        ns = len(s)
        nt = len(t)
        def plen(word, flag):
            n = len(word)
            best = [0] * (n+1)
            for c in range(n):
                for l, r in [(c, c), (c, c+1)]:
                    while l >= 0 and r < n and word[l] == word[r]:
                        if flag:
                            best[l] = max(best[l], r - l + 1)
                        else:
                            best[r] = max(best[r], r - l + 1)
                        l -= 1
                        r += 1

            return best
        
        bestS = plen(s, True)
        bestT = plen(t, False)
        s = s[::-1]

        dp = [[0]*(ns+1) for _ in range(nt+1)]
        #dp[i][j] = longest matching substring from i from t and j from s

        for i in range(nt-1, -1, -1):
            for j in range(ns-1, -1, -1):
                if t[i] == s[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i+1][j+1])

        res = max(bestS[0], bestT[nt-1])
        for i in range(nt):
            for j in range(ns):
                if dp[i][j] > 0:
                    L = dp[i][j]                    
                    rem_s = bestS[ns - j] if ns - j < ns else 0
                    rem_t = bestT[i - 1] if i - 1 >= 0 else 0
                    res = max(res, 2 * L + max(rem_s, rem_t))

        return res
