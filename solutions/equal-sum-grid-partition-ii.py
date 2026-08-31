from typing import List
from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        # ============================================
        # HORIZONTAL CUTS
        # ============================================

        top = defaultdict(int)
        bottom = defaultdict(int)

        tsum = 0
        bsum = 0

        # Initially everything is in bottom
        for row in grid:
            for x in row:
                bottom[x] += 1
                bsum += x

        # Cut after row r
        # Don't process the last row because bottom
        # must remain non-empty.
        for r in range(rows - 1):
            rs = 0

            # Move row r from bottom -> top
            for c in range(cols):
                x = grid[r][c]

                top[x] += 1
                bottom[x] -= 1

                rs += x

            tsum += rs
            bsum -= rs

            # Already equal
            if tsum == bsum:
                return True

            diff = abs(tsum - bsum)

            # ----------------------------------------
            # Bottom is larger
            # ----------------------------------------
            if bsum > tsum:

                # Bottom consists of exactly one row.
                # Only the two endpoints can be removed
                # without disconnecting the row.
                if r == rows - 2:
                    if (grid[r + 1][0] == diff or
                        grid[r + 1][-1] == diff):
                        return True

                # Bottom has multiple rows, so removing
                # any single cell keeps it connected.
                elif bottom[diff] > 0:
                    return True

            # ----------------------------------------
            # Top is larger
            # ----------------------------------------
            elif tsum > bsum:

                # Top consists of exactly one row.
                # Only the two endpoints can be removed.
                if r == 0:
                    if (grid[0][0] == diff or
                        grid[0][-1] == diff):
                        return True

                # Top has multiple rows, so any cell works.
                elif top[diff] > 0:
                    return True

        # ============================================
        # VERTICAL CUTS
        # ============================================

        left = defaultdict(int)
        right = defaultdict(int)

        lsum = 0
        rsum = 0

        # Initially everything is in right
        for c in range(cols):
            for r in range(rows):
                x = grid[r][c]

                right[x] += 1
                rsum += x

        # Cut after column c
        # Don't process the last column because right
        # must remain non-empty.
        for c in range(cols - 1):
            cs = 0

            # Move column c from right -> left
            for r in range(rows):
                x = grid[r][c]

                left[x] += 1
                right[x] -= 1

                cs += x

            lsum += cs
            rsum -= cs

            # Already equal
            if lsum == rsum:
                return True

            diff = abs(lsum - rsum)

            # ----------------------------------------
            # Right is larger
            # ----------------------------------------
            if rsum > lsum:

                # Right consists of exactly one column.
                # Only the top and bottom cells can be removed.
                if c == cols - 2:
                    if (grid[0][c + 1] == diff or
                        grid[-1][c + 1] == diff):
                        return True

                # Right has multiple columns, so any cell
                # can be removed while keeping it connected.
                elif right[diff] > 0:
                    return True

            # ----------------------------------------
            # Left is larger
            # ----------------------------------------
            elif lsum > rsum:

                # Left consists of exactly one column.
                # Only the top and bottom cells can be removed.
                if c == 0:
                    if (grid[0][0] == diff or
                        grid[-1][0] == diff):
                        return True

                # Left has multiple columns, so any cell works.
                elif left[diff] > 0:
                    return True

        return False