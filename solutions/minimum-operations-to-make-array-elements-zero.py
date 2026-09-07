class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        #4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        #2, 3, 5, 6, 8

        def solve(l, r):
            pl = int(math.log(l, 4))
            freq = {}
            curr = l
            while curr < r:
                nxt = 4 ** (pl + 1)
                if nxt >= r:
                    freq[pl+1] = r - curr + 1
                    break
                freq[pl+1] = nxt - curr + 1
                pl += 1
                curr = nxt
            tot = 0 
            left = []
            for key in freq:
                tot += freq[key]//2 * key
                if freq[key] % 2 == 1:
                    left.append(key)
            left.sort()
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
            
            

            
            


