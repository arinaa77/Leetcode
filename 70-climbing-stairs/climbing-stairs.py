class Solution:
    def climbStairs(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 1:
            return n

        dp = [0] * 3

        dp[1] = 1
        dp[2] = 2

        for _ in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total

        return dp[2]

        '''
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]
        '''