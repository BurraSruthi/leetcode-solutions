class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # left_best[i][j]:
        # max(sum(i..k) + dp[i][k]) for k <= j
        left_best = [[0] * n for _ in range(n)]

        # right_best[i][j]:
        # max(sum(k..j) + dp[k][j]) for k >= i
        right_best = [[0] * n for _ in range(n)]

        # Base case: one stone
        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):

            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # Check whether ALL splits have left < right
                last_left = prefix[j] - prefix[i]

                if 2 * last_left < total:
                    dp[i][j] = left_best[i][j - 1]
                    continue

                # Find first k where left >= right
                lo = i
                hi = j - 1

                while lo < hi:
                    mid = (lo + hi) // 2

                    left = prefix[mid + 1] - prefix[i]

                    if 2 * left < total:
                        lo = mid + 1
                    else:
                        hi = mid

                k = lo

                left = prefix[k + 1] - prefix[i]

                # For left >= right region
                ans = right_best[k + 1][j]

                # If exactly equal, both sides are possible
                if 2 * left == total:
                    ans = max(
                        ans,
                        left_best[i][k]
                    )

                # Splits before k have left < right
                elif k > i:
                    ans = max(
                        ans,
                        left_best[i][k - 1]
                    )

                dp[i][j] = ans

            # Build helper arrays for future intervals
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                value = total + dp[i][j]

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    value
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    value
                )

        return dp[0][n - 1]