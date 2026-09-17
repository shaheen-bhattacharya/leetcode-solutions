class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tail = []
        n = len(nums)

        res = 0
        for i in range(n):
            pos = bisect_left(tail, nums[i])
            if pos == len(tail):
                tail.append(nums[i])
            else:
                tail[pos] = nums[i]
        return len(tail)