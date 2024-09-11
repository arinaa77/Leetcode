class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Time: O(logn)
        # Space: O(logn)

        # Count bit difference, O(1)
        xor_result = start ^ goal
        # Find binary representation of xor result, O(logn)
        binary_result = bin(xor_result)
        # count number of 1 in binary representation, O(logn)
        result = binary_result.count('1')
        return result