class Solution:
    def compress(self, chars: List[str]) -> int:
        # Time: O(n)
        # Space: O(1)
        left = 0
        cnt = 1

        for right in range(1, len(chars) + 1):
            if right < len(chars) and chars[right] == chars[right - 1]:
                cnt += 1
            else:
                chars[left] = chars[right - 1]
                left += 1

                if cnt > 1:
                    for digit in str(cnt):
                        chars[left] = digit
                        left += 1
                cnt = 1

        return left