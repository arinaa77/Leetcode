class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2)
        
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        result = 0
        for i in range(len(dp)):
            result = max(result, dp[i])
        return result
        
