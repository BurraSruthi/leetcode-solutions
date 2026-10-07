class Solution:
    def ways(self, n, dp):
        if n <= 1:
            return dp[n]

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.ways(n - 1, dp) + self.ways(n -2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1
        
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        self.ways(n, dp)
        return dp[n]