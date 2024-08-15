class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)

        if len(nums) == 1:
            return True

        cover = 0

        for i in range(len(nums)):
            if i <= cover:
                cover = max(cover, i + nums[i])
                if cover >= len(nums) - 1:
                    return True
        
        return False