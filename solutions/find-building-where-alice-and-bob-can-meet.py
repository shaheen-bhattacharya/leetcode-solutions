class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        stack = []
        nq = len(queries)
        n = len(heights)
        for i in range(nq):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            queries[i] = [a, b, i]
        queries.sort(key = lambda x: x[1])  

        res = [0] * (nq)

        hi = n-1
        print(queries)
        for i in range(nq-1, -1, -1):
            print(i)
            if a == b:
                continue
            a, b, ix = queries[i]
            while hi >= b:
                while stack and heights[hi] > heights[stack[-1][0]]:
                    stack.pop()
                stack.append((heights[hi], hi))
                hi -= 1
            print(stack)

            l, r = 0, len(stack) 
            need = max(heights[a], heights[b])
            while l < r:
                m = (l + r) // 2
                hgt, idx = stack[m]
                if hgt < need:
                    l = m + 1
                else:
                    r = m
            if l == len(stack):
                res[ix] = -1
            else:
                res[ix] = stack[l][1]
        return res
            
                




