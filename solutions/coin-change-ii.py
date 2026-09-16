class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in range(amount + 1):
            for v in coins:
                
                dp[c] += dp[c-v]
        return dp[amount]