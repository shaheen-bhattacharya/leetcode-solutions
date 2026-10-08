class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        LOG = k.bit_length()
        sm = [[0]*(LOG+1) for _ in range(n)]
        up = [[0]*(LOG+1) for _ in range(n)]

        for i in range(n):
            up[i][0] = receiver[i]
            sm[i][0] = receiver[i]
        
        for p in range(1, LOG+1):
            for i in range(n):
                prev = up[i][p-1]
                up[i][p] = up[prev][p-1]
                sm[i][p] = sm[i][p-1] + sm[prev][p-1]

        res = 0
        for i in range(n):
            cnt = 0
            for p in range(k.bit_length()):
                if k & (1 << p):
                    cnt += sm[i][p]
            res = max(res, cnt)
        return res
