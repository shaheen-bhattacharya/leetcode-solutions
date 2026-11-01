class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def value(num):
            return (num*(num+1))//2
        
        dp = [[inf] * (k+1) for _ in range(n+1)]
        pref = [0] + list(accumulate(nums))
        """
        2*v(a-b) = a^2 - ab + a - ab + b^2 - b 
        = (a^2 + a)/2 + (b^2 - b)/2 - ab

        minimize (dp[i][u]+ over i+1 to n and u from )
        """

        dp[n][k] = 0

        def query(hull, x):
            while len(hull) >= 2:
                m1, c1 = hull[0]
                m2, c2 = hull[1]
                if m1 * x + c1 >= m2 * x + c2:
                    hull.popleft()
                else:
                    break
            m, c = hull[0]
            return m * x + c
        
        def insert(hull, m, c):
            while len(hull) >= 2:
                m1, c1 = hull[-2]
                m2, c2 = hull[-1]
                if (c2 - c1) * (m - m2) >= (c - c2) * (m2 - m1):
                    hull.pop()
                else:
                    break
            hull.append((m, c))

        for u in range(k-1, -1, -1):
            hull = deque()
            for i in range(n-1, -1, -1):
                t = i + 1
                a = pref[t]
                m = -a
                c = value(a) + dp[t][u+1]
                x = pref[i]
                if hull:
                    dp[i][u] = query(hull, x) + value(x)
        return dp[0][0]
