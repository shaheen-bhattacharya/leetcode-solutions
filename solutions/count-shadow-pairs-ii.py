class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)
        res = n - 1
        nxt = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
            stack.append(i)
        print(nxt)