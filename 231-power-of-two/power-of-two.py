class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bitwise operation: AND (&) operation compares each bit of two numbers
        # Time: O(1)
        # Space: O(1)

        if n > 0 and (n & (n - 1) == 0):
            return True