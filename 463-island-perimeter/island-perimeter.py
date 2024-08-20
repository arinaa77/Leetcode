class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(n * m)
        # Space: O(1)

        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                # Check for island
                if grid[i][j] == 1:
                    perimeter += 4
                    # Check if above is also island, remove duplicate area
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    # Check if left is also island, remove duplicate area
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter