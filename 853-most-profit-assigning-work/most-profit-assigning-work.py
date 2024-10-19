class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Time: O(nlogn + mlogm)
        # Space: O(n)
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        i = 0
        max_profit = 0
        total_profit = 0

        for w in worker:
            while i < len(jobs) and w >= jobs[i][0]:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit

        return total_profit