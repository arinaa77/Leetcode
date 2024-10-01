class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start_ind, path, result):
            result.append(path[:])

            for i in range(start_ind, len(nums)):
                # dedup on same level
                if i > start_ind and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1, path, result)
                path.pop()

        result = []
        # Sort the array for dedup
        nums.sort()
        backtrack(nums, 0, [], result)
        return result