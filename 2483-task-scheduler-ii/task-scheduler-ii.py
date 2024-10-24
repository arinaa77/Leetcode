class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # Time: O(n)
        # Space: O(n)
        result = 0
        records = defaultdict(int)

        for task in tasks:
            result += 1
            
            if task in records:
                diff = result - records[task]
                if diff <= space:
                    result += (space - diff + 1)
            records[task] = result

        return result