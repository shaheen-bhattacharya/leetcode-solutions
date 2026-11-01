class Solution:
    def countEffective(self, nums: List[int]) -> int:
        """
        [1, 2, 3]
        [01, 10, 11] => 11
        """
        n = len(nums)
        MOD = 1_000_000_007
        groups = defaultdict(list)
        for i in range(n):
            num = nums[i]
            while num > 0:
                key = num & -num
                groups[key].append(i)
                num -= key
        print(groups)