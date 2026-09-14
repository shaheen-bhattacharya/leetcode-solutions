class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque([(nums[-1], 1)])
        cost = 0
        r = len(nums) - 1

        res = 0
        for i in range(n-2, -1, -1):
            c=1
            #process left
            while q and q[-1][0] < nums[i]:
                prev, pc = q.pop()
                c += pc
                cost += pc * (nums[i] - prev)
            q.append((nums[i], c))

            #process right
            while cost > k:
                top, tc = q.popleft()
                r -= 1
                tc -= 1
                cost -= (top - nums[r])
                if tc > 0:
                    q.append((top, tc))
            res += r - i + 1
        return res
                






