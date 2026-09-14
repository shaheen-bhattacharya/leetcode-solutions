class Solution:
    def minOperations(self, nums: list[int]) -> int:
        #4584891
        ops = 0
        for num in nums:
            snum = str(num)
            sn = len(snum)
            if sn == 1:
                continue
            fst = snum[:sn//2]
            rf = int(fst[::-1])
            snd = snum[(sn+1)//2:]
            nsn = int(snd)
            
            if sn % 2 == 0:
                if nsn <= rf:
                    res = f"{fst}{rf}"
                    nf = str(int(fst)-1)
                    nnf = nf
                    if nf[0] == "-":
                        nnf = nf[1:-1]
                    res2 = f"{nf}{nnf}"
                else:
                    nf = str(int(fst)+1)
                    res = f"{nf}{nf[::-1]}"
                    res2 = f"{fst}{rf}"
            else:
                if nsn <= rf:
                    res = f"{fst}{snum[sn//2]}{rf}"
                    nf = str(int(snum[:sn//2+1])-1)
                    nnf = nf
                    if nf[0] == "-":
                        nnf = nf[1:-1]
                    res2 = f"{nf}{nnf[::-1]}"
                else:
                    nf = str(int(snum[:sn//2+1])+1)
                    res = f"{nf}{nf[:-1][::-1]}"
                    res2 = f"{fst}{snum[sn//2]}{rf}"
            print(num, res, res2)
            ops += min(int(res) - num, num - max(8 if int(res2) % 2 == 0 else 9, int(res2)))//2
            print(ops)
        return ops
                    
            