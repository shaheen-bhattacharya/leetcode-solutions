class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tail = []
        n = len(nums)
        sl = SortedList()

        res = 0
        for i in range(n):
            sl.add(nums[i])
            print(nums[i], sl, i)
            idx = sl.bisect_left(nums[i])
            res = max(res, idx)
        return res