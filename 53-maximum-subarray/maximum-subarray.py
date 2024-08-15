class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)

            # If curr_sum is negative, disgard this set by setting curr_sum to 0
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

        '''
        # Brute Force
        # Time: O(n^2)

        max_count = float('-inf')
        curr_count = 0

        for i in range(len(nums)):
            curr_count = 0
            for j in range(i, len(nums)):
                curr_count += nums[j]
                max_count = max(curr_count, max_count)
        
        return max_count
        '''