class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        #4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        #2, 3, 4, 5, 6
        #1, 1, 2, 2, 2

        def solve(l, r):
            pl = int(math.log(l, 4))
            curr = l
            tot = 0
            while curr <= r:
                nxt = 4 ** (pl + 1)
                if nxt-1 >= r:
                    tmp = r - curr + 1
                else:
                    tmp = nxt - curr
                print(tmp)
                tot += tmp ** (pl+1)
                pl += 1
                curr = nxt

            return ceil(tot/2)
        
        res = 0
        for l, r in queries:
            res += solve(l, r)
        return res
            
            

            
            


