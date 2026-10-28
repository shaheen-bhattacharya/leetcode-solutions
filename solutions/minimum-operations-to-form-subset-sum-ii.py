class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        """
        continuous // then only *
        """
        n = len(nums)
        cost = defaultdict(list)
        seen = set()
        for i in range(n):
            num = nums[i]
            if num in seen:
                continue
            seen.add(num)
            best = {}
            key = nums[i]
            cost[key].append((key, 0))
            ops = 0
            while num > 1:
                ops += 1
                num//=2
                best[num] = ops if num not in best else min(ops, best[num])
                tmp = num  
                top = ops
                while tmp < sm:
                    tmp *= 2
                    top += 1
                    best[tmp] = top if tmp not in best else min(top, best[tmp])
                for k in best:
                    cost[nums[i]].append((k, best[k]))
    
        print(cost)
        dp = [inf] * (sm+1)
        dp[0] = 0
        for key in nums:
            ndp = [inf]*(sm+1)
            ndp[0] = 0
            for v, c in cost[key]:
                for i in range(sm+1):
                    if i < v:
                        ndp[i] = min(ndp[i], dp[i])
                        continue
                    ndp[i] = min(ndp[i], dp[i], dp[i-v]+c)
            dp = ndp[:]
        return dp[sm] if dp[sm] != inf else -1

                


