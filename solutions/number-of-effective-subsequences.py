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
                groups[key].add(i)
                num -= key
        nb = len(groups)
        keys = sorted(groups.keys())
        print(groups)
        mv = max(keys)
        # dp = [0] * nb
        # 1 2 |2 3 |3 4 |5 2 6| 4 5 6|
        res = 0
        for mask in range(1, 2<<nb+1):
            unique = set()
            good = True
            while mask > 0:
                b = mask & -mask
                flag = False
                for v in groups[b]:
                    if v not in unique:
                        flag = True
                        break
                if not flag:
                    good = False
                    break
                mask -= b
            res += good
        return res


        

        



