class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(n^2)

        n = len(grid)
        # Count how many times each row appears
        cnt = Counter(tuple(row) for row in grid)

        result = 0
        # Check number of time each column appears
        for j in range(n):
            result += cnt[tuple([grid[i][j] for i in range(n)])]
        
        return result