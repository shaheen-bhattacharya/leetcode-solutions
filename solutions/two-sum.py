class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                return [i, seen[target-num]]
            seen[num] = i

        