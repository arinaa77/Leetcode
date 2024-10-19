class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Time: O(n)
        # Space: O(1)
        def getManhattanDistance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        min_dist = float("inf")
        min_index = -1

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                curr_dist = getManhattanDistance(p, [x, y])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    min_index = i
        
        return min_index