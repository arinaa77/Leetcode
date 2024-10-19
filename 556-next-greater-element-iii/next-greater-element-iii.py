class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        digits = list(str(n))
        length = len(digits)

        #Find the first digit smaller than it's right as pivot
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        # If no pivot, curr num is the largest
        if i == -1:
            return -1
        
        # Find the rightmost digit larger than pivot
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Perform swap
        digits[i], digits[j] = digits[j], digits[i]
        # Reverse part after pivot
        digits = digits[:i + 1] + digits[i + 1:][::-1]

        result = int("".join(digits))
        return result if result <= 2 ** 31 - 1 else -1
        