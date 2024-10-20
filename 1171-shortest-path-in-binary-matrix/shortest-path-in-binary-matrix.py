class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1] != 0:
            return -1
        
        queue = deque([(0, 0, 1)])
        visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            x, y, dist = queue.popleft()

            if x == n - 1 and y == n - 1:
                return dist
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))

        return -1