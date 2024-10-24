class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Time: O(m * n)
        # Space: O(m * n)
        m = len(grid)
        n = len(grid[0])

        directions = {
            1: [(0, -1, [1, 4, 6]), (0, 1, [1, 3, 5])],
            2: [(-1, 0, [2, 3, 4]), (1, 0, [2, 5, 6])],
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])],
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],
            5: [(-1, 0, [2, 3, 4]), (0, -1, [1, 4, 6])],
            6: [(-1, 0, [2, 3, 4]), (0, 1, [1, 3, 5])]
        }

        queue = deque([(0, 0)])
        visited = set((0, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy, neighbors in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if grid[nx][ny] in neighbors:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False