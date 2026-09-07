class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        #4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        #2, 3, 4, 5, 6
        #1, 1, 2, 2, 2

        def solve(l, r):
            pl = int(math.log(l, 4))
            freq = {}
            curr = l
            left = []
            tot = 0
            while curr <= r:
                nxt = 4 ** (pl + 1)
                # print(curr, nxt)
                if nxt-1 >= r:
                    freq[pl+1] = r - curr + 1
                else:
                    freq[pl+1] = nxt - curr

                tot += freq[pl+1]//2 * (pl+1)
                if freq[pl+1] % 2 == 1:
                    left.append(pl+1)
                pl += 1
                curr = nxt

            # print(freq)
            # print(left)
            for i in range(len(left) - 1):
                tot += left[i]
                left[i+1] -= left[i]
            if left:
                tot += left[-1]
            return tot
        
        res = 0
        for l, r in queries:
            res += solve(l, r)
        return res
            
            

            
            


