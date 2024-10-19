class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        if len(nums) < 2:
            return 0
        
        nums.sort()
        max_diff = -float('inf')
        left, right = 0, 1

        while right < len(nums):
            max_diff = max(max_diff, nums[right] - nums[left])
            left += 1
            right += 1
        
        return max_diff
