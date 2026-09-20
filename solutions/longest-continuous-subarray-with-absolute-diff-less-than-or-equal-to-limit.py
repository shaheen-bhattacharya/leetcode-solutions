class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        q = deque()
        n = len(nums)
        l = 0
        res = 0
        for r in range(n):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            while nums[q[-1]] - nums[q[0]] > limit:
                l = q[0] + 1
                q.popleft()
            print(q)
            res = max(res, r - l + 1)
        return res
            
