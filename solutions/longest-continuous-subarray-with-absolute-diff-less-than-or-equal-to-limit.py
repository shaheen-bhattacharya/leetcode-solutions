class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        q = deque()
        qinc = deque()
        n = len(nums)
        l = 0
        res = 0
        for r in range(n):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            while qinc and nums[r] <= nums[qinc[-1]]:
                qinc.pop()
            qinc.append(r)
            while nums[q[0]] - nums[qinc[0]] > limit:
                if l == q[0]:
                    q.popleft()
                if l == qinc[0]:
                    qinc.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
            
