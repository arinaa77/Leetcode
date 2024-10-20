class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n)
        # Space: O(m * n)
        m = len(mat)
        n = len(mat[0])

        result = [[-1] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
            
                if 0 <= nx < m and 0 <= ny < n and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))
        
        return result