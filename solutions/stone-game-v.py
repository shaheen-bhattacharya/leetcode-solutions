class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] + list(accumulate(stoneValue))
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n+1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                res = 0
                for i in range(l, r):
                    leftSum = pref[i + 1] - pref[l]
                    rightSum = pref[r + 1] - pref[i + 1]
                    if leftSum < rightSum:
                        res = max(res, leftSum + dp[l][i])
                    elif rightSum < leftSum:
                        res = max(res,rightSum + dp[i + 1][r])
                    else:
                        res = max(res,leftSum + dp[l][i],rightSum + dp[i + 1][r])
                dp[l][r] = res
        return dp[0][n-1]
        