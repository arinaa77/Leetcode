class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Time: O(n)
        # Space: O(1)

        result = []
        n = len(nums)

        i = 0
        while i < n:
            start = i
            # Find the current range of consective nums
            while i < n - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            
            # Construct the string
            s = str(nums[start])

            # Check if there are consectives to append
            if i > start:
                s += '->' + str(nums[i])

            result.append(s)
            i += 1
        
        return result