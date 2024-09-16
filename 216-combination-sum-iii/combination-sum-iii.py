class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(target_sum, k, curr_sum, start_ind, path, result):
            if curr_sum > target_sum:
                return

            if len(path) == k:
                if curr_sum == target_sum:
                    result.append(path[:])
                return

            for i in range(start_ind, 9 - (k - len(path)) + 2):
                curr_sum += i
                path.append(i)
                backtrack(target_sum, k, curr_sum, i + 1, path, result)
                curr_sum -= i
                path.pop()
        
        result = []
        backtrack(n, k, 0, 1, [], result)
        return result