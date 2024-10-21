class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        # Level-wise BFS
        m, n = len(grid), len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        result = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            # Process oranges based on level
            # Increment result based on level, not amount of oranges
            size = len(queue)
            new_rotting = False

            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        new_rotting = True

            if new_rotting:
                result += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return result