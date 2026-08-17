class Solution:
    def kthDigit(self, k: int) -> int:
        #9, 2 * 9 * 10^1, 3 * 9 * 10^2, 4 * 9 * 10^3
        if k <= 9:
            return k
        k -= 9

        #d * 9 * 10^(d-1), d >= 2
        d = 2
        while k > 0:
            blocks = 9 * 10**(d-2)
            amt = d * 10 * blocks
            if k - amt <= 0:
                break
            k -= amt
            d+=1
        #119th digit in the 3 digits
        off = (k - 1) // (10 * d)
        # print(k, d, off)
        b = 10**(d-2) + off
        s = ""
        if b % 2 == 0:
            upper = 10 * b + 9 + 1
            lower = 10 * b
            ch = 1
        else:
            lower = 10 * b + 9
            upper = 10 * b - 1
            ch = -1

        for num in range(lower, upper, ch):
            s += str(num)
        # print(s)
        return int(s[k % (10 * d) - 1])
            

        