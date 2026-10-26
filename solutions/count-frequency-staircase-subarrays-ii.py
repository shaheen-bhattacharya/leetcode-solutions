class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        max_dist = [0] * (n + 1)
        k = 1
        for rem in range(1, n + 1):
            if (k + 1) * (k + 2) // 2 <= rem:
                k += 1
            max_dist[rem] = k
        ans = 0
        pos = [-1] * (1 + max(nums))
        f = []
        for i in range(n):
            f = []
            ok = 0
            max_d = max_dist[n - i]
            seen = []
            for j in range(i,n):
                if pos[nums[j]] == -1:
                    f.append(0)
                    pos[nums[j]] = len(f) - 1
                    seen.append(nums[j])
                if len(f) > max_d:
                    break
                p = pos[nums[j]]
                f[p] += 1
                if f[p] > p + 1:
                    break
                if f[p] == p + 1:
                    ok += 1
                if ok == len(f):
                    ans += 1
            for x in seen:
                pos[x] = -1
        return ans