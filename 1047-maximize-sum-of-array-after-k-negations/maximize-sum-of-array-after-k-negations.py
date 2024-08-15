class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(1)

        # Sort the list in descending order by abs value
        nums.sort(key=lambda x: abs(x), reverse=True)

        # Change negative values only
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        
        # Check for remaining k, change the samllest value
        # Only needed when k is odd
        if k % 2 == 1:
            nums[-1] *= -1
        
        return sum(nums)