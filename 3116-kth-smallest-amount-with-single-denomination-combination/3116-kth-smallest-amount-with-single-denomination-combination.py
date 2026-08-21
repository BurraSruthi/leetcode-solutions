class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # LCM of two numbers
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                val = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        val = lcm(val, coins[i])
                        bits += 1

                        if val > x:
                            break

                if val > x:
                    continue

                if bits % 2 == 1:
                    ans += x // val
                else:
                    ans -= x // val

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left