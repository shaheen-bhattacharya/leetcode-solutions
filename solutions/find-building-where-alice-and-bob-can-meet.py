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
        for i in range(nq-1, -1, -1):
            a, b, ix = queries[i]
            if a == b:
                res[ix] = a
                continue
            while hi >= b:
                while stack and heights[hi] > stack[-1][0]:
                    stack.pop()
                stack.append((heights[hi], hi))
                hi -= 1

            l, r = 0, len(stack) 
            need = max(heights[a], heights[b])
            if heights[a] == need and need == stack[0][0]:
                res[ix] = -1
                continue
            cond = heights[a] != heights[b]
            while l < r:
                m = (l + r) // 2
                hgt, idx = stack[m]
                if (cond and need <= hgt) or ((not cond) and need < hgt):
                    l = m + 1
                else:
                    r = m
            val = stack[l-1]
            
            if l == 0:
                res[ix] = -1
            else:
                res[ix] = stack[l-1][1]
        return res
            
                




