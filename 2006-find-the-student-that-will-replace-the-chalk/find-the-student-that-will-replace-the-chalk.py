class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        
        total_needed = sum(chalk)
        k %= total_needed

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]