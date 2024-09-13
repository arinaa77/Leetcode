class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        if len(nums) == 1:
            return 0
        
        n = len(nums)
        min_index = 0
        max_index = 0

        for i in range(n):
            # To ensure minimum sawp
            # Find first occr of min element
            if nums[i] < nums[min_index]:
                min_index = i
            # Find last occr of max element
            if nums[i] >= nums[max_index]:
                max_index = i
        
        swaps = min_index + (n - 1 - max_index)

        if min_index > max_index:
            swaps -= 1
        
        return swaps