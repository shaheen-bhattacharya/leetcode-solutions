class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        n = len(availableIntervals)
        availableIntervals.sort()
        targetIntervals.sort()

        fa = []
        for i in range(n-1):
            if availableIntervals[i][0] == availableIntervals[i+1][0]:
                continue
            fa.append(availableIntervals[i])
        fa.append(availableIntervals[-1])
        if len(fa) == 0:
            return -1
        ft = []
        for s, e in targetIntervals:
            if len(ft) == 0:
                ft.append([s, e])
            else:
                ps, pe = ft[-1]
                if s > pe:
                    ft.append([s, e])
                else:
                    ft[-1] = [ps, max(e, pe)]
        
        na = len(fa)
        nt = len(ft)
        i = 0
        j = 0

        aend = 0
        res = 0
        while i < na or j < nt:
            if j == nt:
                break
            ts, te = ft[j]
            if aend >= te:
                j += 1
                continue
            if i == na:
                return -1
            res += 1
            st = max(aend, ts)
            if i < na:
                ni = i
                while ni < na and fa[ni][0] <= st:
                    aend = max(aend, fa[ni][1])
                    ni += 1
                if ni == i:
                    return -1
                i = ni
        if j == nt:
            return res
        return -1
            
    




        
        