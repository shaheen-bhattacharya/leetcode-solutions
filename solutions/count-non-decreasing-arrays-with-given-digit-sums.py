class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(digitSum)

        def dt(num):
            ret = 0
            while num > 0:
                ret += num % 10
                num //= 10
            return ret

        dp = [0] * 5001 #dp[i] = number of valid arrays ending at i
        for i in range(5001):
            if dt(i) == digitSum[0]:
                dp[i] = 1
        
        for i in range(1, n):
            dsum = digitSum[i]
            ndp = [0] * 5001
            pref = list(accumulate(dp))
            for j in range(5001):
                if dt(j) == dsum:
                    ndp[j] = pref[j]
            dp = ndp
        return sum(dp) % MOD

