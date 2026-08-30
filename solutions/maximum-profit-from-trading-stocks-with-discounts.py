class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u-1].append(v-1)
        dp = [[[0] * (budget+1) for _ in range(2)] for _ in range(n)]

        #dp[i][pbought][b] = max profit for user i if pbought and spending budget b
        
        def merge(c1, c2):
            res = [0] * (budget+1)
            for b1 in range(budget+1):
                for b2 in range(budget+1-b1):
                    res[b1+b2] = max(res[b], c1[b1], c2[b2])
            return res

        def dfs(i):
            for ch in adj[i]:
                dfs(ch)
            
            for pb in (0, 1):
                price = price[i]//2 if pb else price[i]
                profit = future[i] - price[i]

                skip = [0] * (budget + 1)
                for ch in adj[i]:
                    skip = merge(skip, dp[ch][0])
                
                take = [0] * (budget + 1)
                for ch in adj[i]:
                    take = merge(take, dp[ch][1])
                
                best = [0] * (budget + 1)
                for b in range(price, budget+1):
                    best[b] = max(best[b], take[b - price] + profit)

                for b in range(budget+1):
                    dp[i][pb][b] = max(dp[i][pb][b], skip[b], best[b])

        return max(dp[0][0])



            