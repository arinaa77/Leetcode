class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0

        while left < right:
            sum = nums[left] + nums[right]

            if sum == k:
                result += 1
                left += 1
                right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
        
        return result