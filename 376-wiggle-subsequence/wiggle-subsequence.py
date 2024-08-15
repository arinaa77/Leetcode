class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        curr_diff = 0
        pre_diff = 0
        result = 1

        for i in range(len(nums) - 1):
            curr_diff = nums[i + 1] - nums[i]
            if (pre_diff <= 0 and curr_diff > 0) or (pre_diff >= 0 and curr_diff < 0):
                result += 1
                pre_diff = curr_diff

        return result