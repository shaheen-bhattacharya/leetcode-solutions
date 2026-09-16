class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in range(amount, -1, -1):
            for v in coins:
                if c - v >= 0:
                    dp[c] += dp[c-v]
        # print(dp)
        return dp[amount]