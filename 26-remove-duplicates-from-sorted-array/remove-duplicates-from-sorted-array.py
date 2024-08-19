class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n)
        # Spance: O(1)

        left, right = 1, 1

        while right < len(nums):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left
        
        
        # k = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k