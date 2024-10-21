class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid1), len(grid1[0])
        islands_cnt = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid2[i][j] == 0:
                return
            grid2[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    islands_cnt += 1
        
        return islands_cnt