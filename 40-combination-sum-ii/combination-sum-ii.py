class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, curr_sum, start_ind, path, result):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(path[:])
                return

            for i in range(start_ind, len(candidates)):
                # Check for uniqueness
                if i > start_ind and candidates[i] == candidates[i - 1]:
                    continue

                curr_sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, curr_sum, i + 1, path, result)
                curr_sum -= candidates[i]
                path.pop()

        result = []
        # Need to sort candidates for duplicate check
        candidates.sort()
        backtrack(candidates, target, 0, 0, [], result)
        return result