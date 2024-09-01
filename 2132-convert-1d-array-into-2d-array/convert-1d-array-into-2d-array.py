class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Time: O(m * n)
        # Space: O(m * n)
        if len(original) != m * n:
            return []

        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i + n])
        
        return result
