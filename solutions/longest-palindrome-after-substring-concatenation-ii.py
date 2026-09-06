class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)
        
        # Returns max palindrome length ending at or starting at each index
        def plen(word, start_flag):
            n = len(word)
            best = [0] * (n + 1)
            for c in range(n):
                for l, r in [(c, c), (c, c + 1)]:
                    while l >= 0 and r < n and word[l] == word[r]:
                        length = r - l + 1
                        if start_flag:
                            best[l] = max(best[l], length)
                        else:
                            best[r] = max(best[r], length)
                        l -= 1
                        r += 1
            return best

        # bestS[i]: max palindrome in s starting at i
        # bestT[j]: max palindrome in t ending at j
        bestS = plen(s, True)
        bestT = plen(t, False)

        # dp[i][j]: max match length for prefix of t starting at i and suffix of s ending at j
        dp = [[0] * ns for _ in range(nt)]
        
        for i in range(nt - 1, -1, -1):
            for j in range(ns):
                if t[i] == s[j]:
                    prev = dp[i + 1][j - 1] if i + 1 < nt and j - 1 >= 0 else 0
                    dp[i][j] = prev + 1

        res = max(bestS[0], bestT[nt - 1])

        for i in range(nt):
            for j in range(ns):
                if dp[i][j] > 0:
                    L = dp[i][j]
                    
                    # Remaining palindrome in s after index j (starts at j + 1)
                    rem_s = bestS[j + 1] if j + 1 < ns else 0
                    
                    # Remaining palindrome in t before index i (ends at i - 1)
                    rem_t = bestT[i - 1] if i - 1 >= 0 else 0

                    res = max(res, 2 * L + max(rem_s, rem_t))

        return res