class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        max_profit = 0

        for i in range(1, len(prices)):
            # Only include positive profits
            max_profit += max(prices[i] - prices[i - 1], 0)

        return max_profit