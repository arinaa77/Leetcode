class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
        '''
        # Time: O(1)
        # Spance: O(n)
        
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left