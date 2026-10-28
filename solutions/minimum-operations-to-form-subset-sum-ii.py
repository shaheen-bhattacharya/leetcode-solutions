class Solution:
    def minOperations(self, nums: list[int], sm: int) -> int:
        """
        continuous // then only *
        """
        n = len(nums)
        cost = defaultdict(list)
        values = defaultdict(set)
        for i in range(n):
            num = nums[i]
            key = nums[i]
            cost[key].append((key, 0))
            values[key].add(key)
            ops = 0
            while num > 1:
                ops += 1
                num//=2
                if num not in values[key]:
                    values[key].add(num)
                    cost[key].append((num, ops))
                
            while num < sm:
                ops += 1
                if num not in values[key]:
                    values[key].add(num)
                    cost[key].append((num, ops))
                num *= 2
        print(cost)

