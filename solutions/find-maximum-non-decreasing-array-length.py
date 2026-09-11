class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        #1, 2, 3, 4, 99, 999, 3, 99999, 99999999
        n = len(nums)
        prev = nums[0]
        tot = 1
        i = 1
        while i < n:
            curr = 0
            while i < n and curr < prev:
                curr += nums[i]
                i += 1
            tot += 1
            prev = curr
            if curr < prev:
                print("d")
                tot -= 1
        return tot
