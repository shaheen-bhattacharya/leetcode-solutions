class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
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
        for i in range(151):
            while i > 0:
                factors[i].add(lp[i])
                i //= lp[i]
        print(factors)
                 