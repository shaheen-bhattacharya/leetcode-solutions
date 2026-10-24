class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)

        idxl = defaultdict(list)
        fl = defaultdict(SortedList)
        res = 0
        for i in range(n):
            ch = s[i]
            idxl[ch].append(i)
            for c in idxl:
                fl[i].add(idxl[c][-1])
                
        idxr = defaultdict(list)
        fr = defaultdict(SortedList)
        for i in range(n-1, -1, -1):
            ch = s[i]
            idxr[ch].append(i)
            for c in idxr:
                fr[i].add(idxr[c][-1])
            print(idxr)

        res = 0
        for i in range(n-1):
            sl1, sl2 = fl[i], fr[i+1]
            
            if len(sl1) < len(sl2):
                sl1.add(-1)
            elif len(sl1) > len(sl2):
                sl2.add(n)
            else:
                sl1.add(-1)
                sl2.add(n)
            
            print(i, sl1, sl2)
            dist = min(len(sl1), len(sl2))
            # res += 1
            for d in range(dist-1):
                d1 = sl1[-d-1] - sl1[-d-2]
                d2 = sl2[d+1] - sl2[d]
                res += d1 * d2
                
        return res
                
            
            
        
        
                
                    
            
            


                
            
        



            
        
        