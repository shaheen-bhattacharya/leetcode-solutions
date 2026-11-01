class Solution:
    def countEffective(self, nums: List[int]) -> int:
        """
        [1, 2, 3]
        [01, 10, 11] => 11
        110111011111
        """
        n = len(nums)
        MOD = 1_000_000_007
        groups = defaultdict(set)
        for i in range(n):
            num = nums[i]
            while num > 0:
                key = num & -num
                groups[int(math.log2(key))].add(i)
                num -= key
        nb = len(groups)
        dp = [0] * nb
        print(groups)



