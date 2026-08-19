class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)

        def good(w1, w2):
            for i in range(len(w1)):
                f1, l1 = w1[i], w1[-i-1]
                f2, l2 = w2[i], w2[-i-1]
                if f1 != f2 or l1 != l2:
                    return False
            return True
        
        dp = [0] * n
        res = 0
        print(words)
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if good(words[i], words[j]):
                    dp[i] = dp[j] + 1
                    res += dp[i]
                    break
        return res
                


                