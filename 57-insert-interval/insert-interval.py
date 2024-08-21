class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)

        result = []
        i = 0
        n = len(intervals)

        # Append the part before the interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # If there's overlap, modify the range of newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Append the part after the interval
        # while i < n and intervals[i][0] > newInterval[1]:
        while i < n:
            result.append(intervals[i])
            i += 1

        return result