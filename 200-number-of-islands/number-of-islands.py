class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)

        m, n = len(grid), len(grid[0])
        islands_cnt = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands_cnt += 1
        
        return islands_cnt