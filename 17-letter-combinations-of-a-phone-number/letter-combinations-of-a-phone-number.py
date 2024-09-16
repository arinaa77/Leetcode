class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ['', '', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        if not digits:
            return []
        
        result = []
        def backtrack(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            curr_digit = digits[index]
            possible_letters = mapping[int(curr_digit)]

            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, '')
        return result