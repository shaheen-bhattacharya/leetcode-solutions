class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        #yrtxhrcbaterrt abcuitiutgu
        s = s[::-1]
        ns = len(s)
        nt = len(t)
        def plen(word):
            n = len(word)
            best = [1] * (n+1)
            for c in range(n):
                for l, r in [(c, c), (c, c+1)]:
                    while l >= 0 and r < n and word[l] == word[r]:
                        best[l] = max(best[l], r - l + 1)
                        l -= 1
                        r += 1
            best[-1] = 0
            return best
        
        bestS = plen(s)
        bestT = plen(t)

        dp = [[0]*ns for _ in range(nt)]
        #dp[i][j] = longest matching substring from i from t and j from s
        dp[-1][-1] = s[-1] == t[-1]
        for i in range(nt-2, -1, -1):
            for j in range(ns-2, -1, -1):
                if t[i] == s[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i+1][j+1])
        
        res = 0
        for i in range(nt):
            for j in range(ns):
                res = max(res, dp[i][j] + max(bestS[j+1], bestT[i+1]))
        return res
