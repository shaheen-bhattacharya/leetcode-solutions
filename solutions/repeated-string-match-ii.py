class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        #abababsvdaiufhfeababsv
        nb = len(b)
        na = len(a)
        if nb * y > na * x: return False
        dv = math.ceil(nb/na)
        la = a * min(x, 2*dv)
        nla = len(la)
        lp = [0] * nb
        length = 0
        i = 1
        while i < nb:
            if b[length] == b[i]:
                length += 1
                lp[i] = length
                i += 1
            elif length > 0:
                length = lp[length-1]
            else:
                lp[i] = length
                i += 1 

        length = 0
        i = 0
        good = False
        starts = []
        while i < nla:
            if b[length] == la[i]:
                length += 1 
                i += 1
                if length == nb:
                    starts.append(i-nb)
                    length = lp[length-1]
            elif length > 0:
                length = lp[length-1]
            else:
                i += 1
        if not starts:
            return False

        # print(starts)
        ss = set(starts)
        gst = -1
        for fst in starts:
            if fst not in ss:
                continue
            ss.remove(fst)
            cur = (fst + nb)%nla
            valid = False
            cnt = 1
            if y == 1:
                return True
            while cur in ss:
                ss.remove(cur)
                cur = (cur + nb) % nla
                cnt += 1
                if cnt == y:
                    return True
                if cur == fst:
                    valid = True
                    break
            if valid:
                gst = fst
        if gst == -1:
            return False
        return nb*y+gst <= na*x
        
        


        
