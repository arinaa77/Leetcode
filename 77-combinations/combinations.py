class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(n, k, startInd, path, result):
            if len(path) == k:
                result.append(path[:])
                return
            
            # for i in range(startInd, n + 1):
            for i in range(startInd, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(n, k, i + 1, path, result)
                path.pop()

        result = []
        backtrack(n, k, 1, [], result)
        return result