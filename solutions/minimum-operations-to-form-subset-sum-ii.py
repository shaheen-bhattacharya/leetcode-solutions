class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        """
        continuous // then only *
        """
        n = len(nums)
        cost = defaultdict(list)
        values = defaultdict(set)
        seen = set()
        for i in range(n):
            num = nums[i]
            if num in seen:
                continue
            seen.add(num)
            key = nums[i]
            cost[key].append((key, 0))
            values[key].add(key)
            ops = 0
            while num > 1:
                ops += 1
                num//=2
                if num not in values[key]:
                    values[key].add(num)
                    cost[key].append((num, ops))
                
            while num < sm:
                if num not in values[key]:
                    values[key].add(num)
                    cost[key].append((num, ops))
                num *= 2
                ops += 1
        
        dp = [inf] * (sm+1)
        dp[0] = 0
        for key in cost:
            ndp = [0]*(sm+1)
            for v, c in cost[key]:
                for i in range(sm+1):
                    ndp[i] = min(dp[i], dp[i-v]+c)
        return dp[sm] if dp[sm] != inf else -1

                


