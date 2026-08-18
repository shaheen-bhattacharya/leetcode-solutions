class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        lpos = [[-1] * n for _ in range(n)]
        rpos = [[-1] * n for _ in range(n)]

        # Precompute boundaries
        for l in range(n):
            lp = l - 1
            rp = l

            for r in range(l + 1, n):
                total = pref[r + 1] - pref[l]

                # Last k with left <= right
                while lp + 1 <= r - 1:
                    k = lp + 1
                    left_sum = pref[k + 1] - pref[l]

                    if 2 * left_sum > total:
                        break

                    lp += 1

                # First k with left >= right
                while rp <= r - 1:
                    k = rp
                    left_sum = pref[k + 1] - pref[l]

                    if 2 * left_sum >= total:
                        break

                    rp += 1

                lpos[l][r] = lp
                rpos[l][r] = rp

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                best = 0

                # left <= right
                if lpos[l][r] >= l:
                    best = left_best[l][lpos[l][r]]

                # left >= right
                if rpos[l][r] <= r - 1:
                    best = max(
                        best,
                        right_best[rpos[l][r] + 1][r]
                    )

                dp[l][r] = best

                total = pref[r + 1] - pref[l]

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + total
                )

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + total
                )

        return dp[0][n - 1]