class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def sieve(n):
            lp = [0] * (n+1)
            primes = []
            for i in range(2, n+1):
                if lp[i] == 0:
                    lp[i] = i
                    primes.append(i)
                for p in primes:
                    if p * i > n or p > lp[i * p]:
                        break
                    lp[p*i] = p
            return lp, primes

        maxv = max(nums)
        n = len(nums)
        lp, primes = sieve(maxv)
        print(lp, "\n", primes)

        # @cache
        # def isPrime(num):


        # tree = [0] * (4 * n) 
        # def build(node, l, r):
