class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [stones[0]] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        ans = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans