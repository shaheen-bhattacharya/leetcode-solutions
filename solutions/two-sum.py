class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [i, seen[num]]
            seen[num] = i

        