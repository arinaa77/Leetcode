class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)

        five = 0
        ten = 0
        twenty = 0

        for bill in bills:
            # Count 5
            if bill == 5:
                five += 1
            
            # Count 10
            elif bill == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1
            
            # Count 20
            else:
                # First use 10
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True