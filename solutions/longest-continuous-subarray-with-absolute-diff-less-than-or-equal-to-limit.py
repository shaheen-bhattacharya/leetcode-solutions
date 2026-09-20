class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        stack = []
        ustack = []
        n = len(nums)
        left = [-1] * n
        lpos = [-1] * n
        for i, num in enumerate(nums):
            val = num - limit
            while stack and val <= nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            while ustack and num >= nums[ustack[-1]]:
                ustack.pop()
            if ustack:
                lpos[i] = ustack[-1]
            ustack.append(i)
        
        print(lpos)
        print(left)
        res = 0
        stack = []
        ustack = []
        for i in range(n-1, -1, -1):
            val = num - limit
            rpos, r = n, n
            while stack and val < nums[stack[-1]]:
                stack.pop()
            if stack:
                r = stack[-1]
            stack.append(i)
            while ustack and num > nums[ustack[-1]]:
                ustack.pop()
            if ustack:
                rpos = ustack[-1]
            ustack.append(i)
            print(i, rpos, r)
            res = max(res, min(rpos, r) - max(lpos[i], left[i]) - 1)
        return res

        
            

            
            
