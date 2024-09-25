class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(s, start_ind, path, result):
            if start_ind == len(s):
                result.append(path[:])
                return
            
            for i in range(start_ind, len(s)):
                # Determine if the current substring is palindrome
                if s[start_ind:i + 1] == s[start_ind:i + 1][::-1]:
                    path.append(s[start_ind:i + 1])
                    backtrack(s, i + 1, path, result)
                    path.pop()

        result = []
        backtrack(s, 0, [], result)
        return result