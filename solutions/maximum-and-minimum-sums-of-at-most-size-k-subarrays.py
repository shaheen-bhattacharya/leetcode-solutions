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
            L = i - lb
            R = rb - i

            a = min(L, k)
            b = min(R, k)

            if a > b:
                a, b = b, a

            return a * b - max(0, (a + b - k) * (a + b - k + 1) // 2)


        res = 0
        for i in range(n):
            lbn = max(i-k, leftmn[i])
            lbx = max(i-k, leftmx[i])
            rbn = min(i+k, rightmn[i])
            rbx = min(i+k, rightmx[i])
            res += nums[i] * solve(lbn, i, rbn) + nums[i] * solve(lbx, i, rbx)
        return int(res)

