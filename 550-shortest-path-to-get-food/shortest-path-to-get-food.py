class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])

        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    start = (i, j)
                    break
            if start:
                break
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque([(start[0], start[1], 0)])
        visited = set()
        visited.add(start)

        while queue:
            x, y, dist = queue.popleft()

            if grid[x][y] == '#':
                return dist
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != "X":
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))

        return -1