class Solution:
    def countEffective(self, nums: List[int]) -> int:
        """
        [1, 2, 3]
        [01, 10, 11] => 11
        """
        MOD = 1_000_000_007
        print(nums[0].bit_count())

