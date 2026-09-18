class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        n = len(words)
        dp = {}
        def dfs(i, left):
            key = (i, left)
            if key in dp:
                return dp[key]
            if i == n:
                return 0
            skip = dfs(i+1, left)
            l2 = list(left)
            curr = 0
            bad = False
            for ch in words[i]:
                idx = ord(ch) - ord('a')
                if l2[idx] == 0:
                    bad = True
                    break
                l2[idx] -= 1
                curr += score[idx]
            take = -inf
            if not bad:
                take = curr + dfs(i+1, tuple(l2))
            dp[key] = max(skip, take)
            return dp[key]

        left = [0]*26
        for ch in letters:
            left[ord(ch) - ord('a')] += 1
        return dfs(0, tuple(left))

            
                
                           




