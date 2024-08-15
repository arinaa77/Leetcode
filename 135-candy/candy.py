class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        candies = [1] * len(ratings)

        # Check candy amount from left to right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Check candy amount from right to left
        # Get max candy amount from the two
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)