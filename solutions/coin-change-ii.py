class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        sc = set(coins)
        coins.sort(reverse=True)

        for c in range(amount+1):
            used = set()
            for v in coins:
                if c - v >= 0 and v not in used:
                    used.add(v)
                    used.add(c-v)
                    dp[c] += dp[c-v]
        print(dp)
        return dp[amount]