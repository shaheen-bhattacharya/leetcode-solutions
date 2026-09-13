class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        stack = []
        n = len(nums)
        pref = [0] + list(accumulate(nums))
        
        left = [-1] * n
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        right = [n] * n
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(n):
            lops = i - left[i]
            l, r = i+1, right[i]
            while l < r:
                m = (l+r)//2
                if pref[m+1] - pref[i+1] <= 4 * (m-i) + k:
                    l = m + 1
                else:
                    r = m
            rops = min(right[i], r) - i
            res += lops * rops
            print(lops, rops)
        return res

