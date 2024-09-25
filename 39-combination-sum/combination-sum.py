class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, curr_sum, start_ind, path, result):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(path[:])
                return
            
            for i in range(start_ind, len(candidates)):
                curr_sum += candidates[i]
                path.append(candidates[i])
                # In recursive calls, start_ind is still i, not i + 1
                # Since same number may be chosen unlimited times
                backtrack(candidates, target, curr_sum, i, path, result)
                curr_sum -= candidates[i]
                path.pop()
        
        result = []
        backtrack(candidates, target, 0, 0, [], result)
        return result