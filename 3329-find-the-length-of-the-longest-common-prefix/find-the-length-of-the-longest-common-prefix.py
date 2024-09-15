class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        cnt = set()

        for num in arr1:
            while num:
                cnt.add(num)
                num //= 10
        
        result = 0
        for num in arr2:
            while num and num not in cnt:
                num //= 10
            result = max(result, num)
        
        return len(str(result)) if result else 0

        '''
        def common_prefix_len(str1, str2):
            i = 0
            while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
                i += 1
            return i
        
        str_arr1 = [str(num) for num in arr1]
        str_arr2 = [str(num) for num in arr2]
        longest_common_prefix = 0

        for str1 in str_arr1:
            for str2 in str_arr2:
                curr_common_prefix = common_prefix_len(str1, str2)
                longest_common_prefix = max(longest_common_prefix, curr_common_prefix)
        
        return longest_common_prefix
        '''