class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        intervals.sort(key=lambda x: x[0])
        non_overlaps = 1

        for i in range(1, len(intervals)):
            # No overlaps
            if intervals[i][0] >= intervals[i - 1][1]:
                non_overlaps += 1
            else:
                # If overlap, update the ending point to the smallest one
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
        
        return len(intervals) - non_overlaps
