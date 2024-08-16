class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(1)

        # Sort the lists based on starting position in ascending order
        points.sort(key=lambda x: x[0])

        result = 1
        for i in range(1, len(points)):
            # If the starting point of the next element is greater than the 
            # range of the current element, update the result
            if points[i][0] > points[i - 1][1]:
                result += 1
            else:
                # If within the range, update the current session's ending point
                points[i][1] = min(points[i][1], points[i - 1][1])

        return result