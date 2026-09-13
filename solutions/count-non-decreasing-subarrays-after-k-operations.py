class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        stack = []
        n = len(nums)
        pref = [0] + list(accumulate(nums))
        dpl = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dpl[i] = dpl[i-1] + 1
        dpr = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                dpr[i] = dpr[i+1] + 1
        
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
            lops = min(i - left[i], dpl[i])
            l, r = i+1, right[i]
            while l < r:
                m = (l+r)//2
                if nums[i] * (m-i) - (pref[m+1] - pref[i+1]) <= k:
                    l = m + 1
                else:
                    r = m
            rops = r - i - 1
            if rops == 1:
                rops += dpr[r-1]
            res += lops * rops
            # print(lops, rops, res)
        return res

