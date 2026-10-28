class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        """
        continuous // then only *
        """
        n = len(nums)
        cost = defaultdict(list)
        values = defaultdict(set)
        for i in range(n):
            num = nums[i]
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

                tmp = num  
                top = ops
                while tmp < sm:
                    tmp *= 2
                    top += 1
                    if tmp not in values[key]:
                        values[key].add(tmp)
                        cost[key].append((tmp, top))
    
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

                


