class Solution:
    def fib(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n <= 1:
            return n

        dp = [0, 1]

        for _ in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total
        
        return dp[1]

        '''
        # Time: O(n)
        # Space: O(n)
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        '''