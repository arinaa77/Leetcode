class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time: O(n)
        # Space: O(1)
        max_avg = -float('inf')
        start = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if (i - start + 1) == k:
                avg = curr_sum / k
                max_avg = max(max_avg, avg)
                curr_sum -= nums[start]
                start += 1

        return max_avg