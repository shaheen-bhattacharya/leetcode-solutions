class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        leftmn = [0]*n
        leftmx = [0]*n
        rightmn = [0]*n
        rightmx = [0]*n

        stack = []
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            leftmx[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            rightmx[i] = stack[-1] if stack else n
            stack.append(i)
        
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            leftmn[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            rightmn[i] = stack[-1] if stack else n
            stack.append(i)

        def solve(lb, i, rb):
            amtl = i - lb - 1
            amtr = rb - i - 1
            if amtl <= amtr:
                s, e = k - amtl - 1, amtr
            else:
                s, e = k - amtr - 1, amtl
            return (s+e)/2 * (s-e+1)


        res = 0
        for i in range(n):
            lbn = max(i-k, leftmn[i])
            lbx = max(i-k, leftmx[i])
            rbn = min(i+k, rightmn[i])
            rbx = min(i+k, rightmx[i])
            res += solve(lbn, i, rbn) + solve(lbx, i, rbx)
        return int(res)

