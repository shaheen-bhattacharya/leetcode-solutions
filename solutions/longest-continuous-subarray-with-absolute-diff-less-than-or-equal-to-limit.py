class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        q = deque()
        qmin = deque()
        n = len(nums)
        l = 0
        res = 0
        for r in range(n):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            while nums[q[0]] - nums[q[-1]] > limit:
                l = q[0] + 1
                q.popleft()
            res = max(res, r - l + 1)
        return res
            
