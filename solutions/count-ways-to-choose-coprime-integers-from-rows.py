class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        rows, cols = len(mat), len(mat[0])
        dp = [[0]*cols for _ in range(rows)]
        factors = defaultdict(set)

        def sieve(n):
            primes = []
            lp = [-1] * (n+1)
            for i in range(2, n+1):
                if lp[i] == -1:
                    lp[i] = i
                    primes.append(i)
                for p in primes:
                    if p > lp[i] or p * i >= n:
                        break
                    lp[i*p] = p
            return primes, lp
        primes, lp = sieve(150)
        for i in range(2, 151):
            k = i
            while i > 1:
                factors[k].add(i)
                i //= lp[i]
        rc = [[0]*151 for _ in range(rows)]
        mt = pow(rows, cols, MOD)
        for r in range(rows):
            for c in range(cols):
                for f in factors[mat[r][c]]:
                    rc[r][f] += 1

        bad = 0
        print(mt, bad)
        for f in range(2, 151): 
            tmp = 1
            for r in range(rows):          
                tmp = (rc[r][f] * tmp) % MOD
            bad = (bad + tmp) % MOD
        return (MOD + mt - bad) % MOD

                 