class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] >= nums[i-1]:
            i += 1
        return i-1
            
            
        